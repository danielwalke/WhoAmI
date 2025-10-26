const titles = [
  "Monkey D. Luffy",
  "Roronoa Zoro",
  "Nami",
  "Usopp",
  "Sanji",
  "Tony Tony Chopper",
  "Nico Robin",
  "Franky",
  "Brook",
  "Jinbe",
  "Portgas D. Ace",
  "Gol D. Roger",
  "Shanks",
  "Buggy",
  "Dracule Mihawk",
  "Boa Hancock",
  "Trafalgar D. Water Law",
  "Eustass Kid",
  "Donquixote Doflamingo",
  "Crocodile",
  "Marshall D. Teach",
  "Sabo",
  "Kaido",
  "Big Mom"
];

export const cards = titles.map((title, index) => ({
  idx: index,
  title: title,
  isActive: true,
  isHidden: false,
}));