#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(function (elt) {
      const name = JSON.parse(characters).name;
      console.log(name);
    });
  }
});
