#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Please provide a valid Movie Id');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const getCharacter = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      }

      if (response.statusCode !== 200) {
        reject(`Invalid status code: ${response.statusCode}`);
      }

      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
};

const fetchCharacters = async () => {
  try {
    const response = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        }

        if (response.statusCode !== 200) {
          reject(`Invalid response code: ${response.statusCode}`);
        }

        resolve(body);
      });
    });

    const movieData = JSON.parse(response);
    const characters = movieData.characters;

    for (let i = 0; i < characters.length; i++) {
      const characterName = await getCharacter(characters[i]);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
};

fetchCharacters();