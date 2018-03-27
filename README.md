## MElt

MElt is a freely available (LGPL) state-of-the-art sequence labeller that is meant to be trained on both an annotated corpus and an external lexicon. It was initially developed by Pascal Denis and Benoît Sagot. Recent evolutions have been carried out by Benoît Sagot. MElt allows for using multiclass Maximum-Entropy Markov models (MEMMs) or multiclass perceptrons (multitrons) as underlying statistical devices. Its output is in the Brown format (one sentence per line, each sentence being a space-separated sequence of annotated words in the word/tag format).

## MElt Docker container

This repository provides a way to contain in a docker container the tool MElt for French Part of Speech tagging.

## Installation

To build the image, run the following command :

``` 
sudo docker build -t melt -f Dockerfile
```

To run a container :

```
sudo docker run -d -p 5000:5000 -it melt
```

The listening will be by default 5000.

## Testing

To test your setup, you can try to `POST` data.
```
curl -H "Content-Type: application/json" -X POST -d '{"data":"Il fait beau dehors. Mais Paris est trop petit pour pouvoir en profiter, et surtout trop cher"}' http://localhost:5000/pos_and_tokenize
```

You should get the output :

```
Il/CLS fait/V beau/ADJ dehors/ADV ./PONCT
Mais/CC Paris/NPP est/V trop/ADV petit/ADJ pour/P pouvoir/VINF en/CLO profiter/VINF ,/PONCT et/CC surtout/ADV trop/ADV cher/ADJ
```

## API Specifications

To interact with the API, you need to `POST` your content in a `JSON` format.

| HTTP METHOD | POST |
| ------------| ---- |
| /pos_and_tokenize | Tokenize and POS tagging |
| /tokenize | Only tokenize |
| /lemma | Lemmatization |

## Tagset

```
ADJ 	   adjective
ADJWH	   interrogative adjective
ADV	   adverb
ADVWH	   interrogative adverb
CC	   coordination conjunction
CLO	   object clitic pronoun
CLR	   reflexive clitic pronoun
CLS	   subject clitic pronoun
CS	   subordination conjunction
DET	   determiner
DETWH	   interrogative determiner
ET	   foreign word
I	   interjection
NC	   common noun
NPP	   proper noun
P	   preposition
P+D	   preposition+determiner amalgam
P+PRO	   prepositon+pronoun amalgam
PONCT	   punctuation mark
PREF	   prefix
PRO	   full pronoun
PROREL	   relative pronoun
PROWH	   interrogative pronoun
V	   indicative or conditional verb form
VIMP	   imperative verb form
VINF	   infinitive verb form
VPP	   past participle
VPR	   present participle
VS	   subjunctive verb form
```

## Credits
- Sagot Benoît et Fišer Darja (2008). Building a free French wordnet from multilingual resources. In Ontolex 2008, Marrakech, Maroc
