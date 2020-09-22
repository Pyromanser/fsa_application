import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import client from './client';

const coordIsValid = (coord) => {
  return !!coord || coord === 0;
};

function Main() {
  const [address, setAddress] = useState('');
  const [geocode, setGeocode] = useState(null);
  const [geocodeError, setGeocodeError] = useState(null);

  const [lat, setLat] = useState(null);
  const [lng, setLng] = useState(null);
  const [resultAddress, setResultAddress] = useState(null);
  const [resultAddressError, setResultAddressError] = useState(null);

  const [startLat, setStartLat] = useState(null);
  const [startLng, setStartLng] = useState(null);
  const [endLat, setEndLat] = useState(null);
  const [endLng, setEndLng] = useState(null);
  const [distance, setDistance] = useState(null);
  const [distanceError, setDistanceError] = useState(null);

  const handleChangeValue = (handler) => (event) => {
    handler(event.target.value);
  };

  const handleGetCoordinates = async (event) => {
    event.preventDefault();

    if (!address) {
      setGeocodeError('Please enter address');
      return;
    }

    try {
      const result = await client.post('http://localhost/api/geo/address-to-geocode/', { address });
      setGeocode(result.data);
      setGeocodeError(null);
    } catch(error) {
      setGeocodeError(error.response.data.detail);
      setGeocode(null);
    }
  }

  const handleGetAddress = async (event) => {
    event.preventDefault();

    if (!coordIsValid(lat) || !coordIsValid(lng)) {
      setResultAddressError('Please enter lat and lng');
      return;
    }

    try {
      const result = await client.post('http://localhost/api/geo/geocode-to-address/', { latlng: [lat, lng] });
      setResultAddress(result.data);
      setResultAddressError(null);
    } catch(error) {
      setResultAddressError(error.response.data.detail);
      setResultAddress(null);
    }
  }

  const handleGetDistance = async (event) => {
    event.preventDefault();

    if (!coordIsValid(startLat) || !coordIsValid(startLng) || !coordIsValid(endLat) || !coordIsValid(endLng)) {
      setDistanceError('Please enter start and end coordinates');
      return;
    }

    try {
      const result = await client.post('http://localhost/api/geo/calc-distance/', { coordinates : [ { latlng: [startLat, startLng] }, { latlng: [endLat, endLng] }]});
      setDistance(result.data.distance);
      setDistanceError(null);
    } catch(error) {
      setDistanceError(error.response.data.detail);
      setDistance(null);
    }
  }

  return (
    <div className="App">
      <h3>FSA Application</h3>
      <hr />
      <div className="section">
        <div className="row">
          <label htmlFor="address" className="label">Address</label>
          <input className="input" type="text" id="address" value={address} onChange={handleChangeValue(setAddress)} />
        </div>
        <button onClick={handleGetCoordinates} className="button row">Get coordinates</button>
        <div className="error row">
          {geocodeError}
        </div>
        {!geocodeError && geocode && geocode.latlng && geocode.latlng.length && (
          <div className="response-field row">
            <div>Latitude: {geocode.latlng[0]}</div>
            <div>Longitude: {geocode.latlng[1]}</div>
          </div>
        )}
      </div>

      <div className="section">
        <div className="row">
          <label htmlFor="lat" className="label">Latitude</label>
          <input className="input" type="number" id="lat" value={lat} onChange={handleChangeValue(setLat)} />
          <label htmlFor="lng" className="label">Longitude</label>
          <input className="input" type="number" id="lng" value={lng} onChange={handleChangeValue(setLng)} />
        </div>
        <button onClick={handleGetAddress} className="button row">Get address</button>
        <div className="error row">
          {resultAddressError}
        </div>
        {!resultAddressError && resultAddress && resultAddress.address && (
          <div className="response-field row">
            <span>{resultAddress.address}</span>
          </div>
        )}
      </div>

      <div className="section">
        <div className="row">
          <label htmlFor="startLat" className="label">Start latitude</label>
          <input className="input" type="number" id="startLat" value={startLat} onChange={handleChangeValue(setStartLat)} />
          <label htmlFor="startLng" className="label">Start longitude</label>
          <input className="input" type="number" id="startLng" value={startLng} onChange={handleChangeValue(setStartLng)} />
        </div>
        <div className="row">
          <label htmlFor="endLat" className="label">End latitude</label>
          <input className="input" type="number" id="endLat" value={endLat} onChange={handleChangeValue(setEndLat)} />
          <label htmlFor="endLng" className="label">End longitude</label>
          <input className="input" type="number" id="endLng" value={endLng} onChange={handleChangeValue(setEndLng)} />
        </div>
        <button onClick={handleGetDistance} className="button row">Get distance</button>
        <div className="error row">
          {distanceError}
        </div>
        {!distanceError && distance && (
          <div className="response-field row">
            <span>Distance: {distance} km</span>
          </div>
        )}
      </div>
    </div>
  );
}

export default Main;
