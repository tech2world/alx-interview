#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Please provide a valid Movie Id');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response code', response.statusCode);
    process.exit(1);
  }

  const MovieData = JSON.parse(body);
  const characters = MovieData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResposne, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResposne.statusCode !== 200) {
        console.error('Invalid status code', charResposne);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
