#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
