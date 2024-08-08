#!/usr/bin/node

// Importation du module 'request' pour faire des requêtes HTTP
const request = require('request');

// Récupération de l'ID du film à partir des arguments de la ligne de commande
// Exemple: Si vous exécutez `./0-starwars_characters.js 3`, 'movieId' vaudra '3'
const mveId = process.argv[2];

// Construction de l'URL de l'API en utilisant l'ID du film
// L'URL finale ressemblera à ceci: 'https://swapi.dev/api/films/3/'
const apilnk = `https://swapi.dev/api/films/${mveId}/`;

// Envoi d'une requête GET à l'API pour récupérer les détails du film
request(apilnk, async function (error, response, body) {
  // Vérification de l'existence d'une erreur dans la requête
  if (error) return console.log(error);

  // Analyse du corps de la réponse pour obtenir les données sous forme d'objet JSON
  const infdata = JSON.parse(body);

  // Extraction de la liste des URLs des personnages du film
  const characters = infdata.characters;

  // Boucle asynchrone pour parcourir chaque URL de personnage
  for (const lnk of characters) {
    // Utilisation d'une promesse pour gérer l'ordre des requêtes
    await new Promise((resolve) => {
      // Envoi d'une requête GET pour chaque URL de personnage
      request(lnk, (error, response, body) => {
        // Vérification de l'existence d'une erreur dans la requête
        if (error) return console.log(error);

        // Analyse du corps de la réponse pour obtenir les détails du personnage
        const charcter = JSON.parse(body);

        // Affichage du nom du personnage
        console.log(charcter.name);

        // Résolution de la promesse pour passer au personnage suivant
        resolve();
      });
    });
  }
});
