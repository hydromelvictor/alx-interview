#!/usr/bin/node
const request = require('request');
const proccess = require('process');

const movie = proccess.argv[2];
const baseUrl = 'https://swapi-api.hbtn.io/api/';
const endpoint = `${baseUrl}/films/${movie}`;

async function starWars() {
  const resp = await request(endpoint).body;
  const film = JSON.parse(resp);
  const characters = film.characters;

  for (let i = 0; i < characters.length; i++) {
    let name_resp = await request(characters[i]).body;
    let name = JSON.parse(name_resp);
    console.log(name.name);
  }
}
