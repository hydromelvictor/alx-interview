#!/usr/bin/node
const request = require('request');

const movie = proccess.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/';
const endpoint = `${baseUrl}/films/${movie}`;

request(endpoint, (error, response, body) => {
  if (!error && response.statusCode == 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((charUrl) => {
      request(charUrl, (error, reponse, body) => {
        if (!error && reponse.statusCode == 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
