#!/usr/bin/node
const request = require('request');
const proccess = require('process');

const movie = proccess.argv[2];
const baseUrl = 'https://swapi-api.hbtn.io/api/';
const endpoint = `${baseUrl}/films/${movie}`;

async function starWars (endpoint) {
  const resp = await request(endpoint).body;
  const film = JSON.parse(resp);
  const characters = film.characters;

  for (let i = 0; i < characters.length; i++) {
    const res = await request(characters[i]).body;
    const name = JSON.parse(res);
    console.log(name.name);
  }
}

starWars(endpoint);
