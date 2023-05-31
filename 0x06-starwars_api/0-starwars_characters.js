#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/';
function validStatus (link) {
  return new Promise(function (resolve, reject) {
    request(link, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main () {
  const film = await validStatus(url + argv[2]);
  const chars = JSON.parse(film).characters;
  chars.forEach(async function (elt) {
    const char = await validStatus(elt);
    const name = JSON.parse(char).name
    console.log(name);
  });
}

main();
