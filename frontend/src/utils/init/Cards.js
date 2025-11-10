function loadImages() {
  const folder = '@/assets/default_cards/';
  const names = [
    'Alex','Amy','Anna','Ben','Dan','Emma','Eva','Jack','Joe','John','Julia',
    'Leo','Lisa','Mark','Mary','Max','Mia','Nina','Paul','Sam','Sara','Sofia','Tim','Tom'
  ];
  const images =  names.map((name, i) => ({
    id: i + 1,
    title: `${name}`,
    url: new URL(`../../assets/default_cards/${name}.png`, import.meta.url).href
  }));
  console.log(images);
  
  return images;
}


export const cards = loadImages().map(image => ({
  id: image.id,
  title: image.title,
  url: image.url,
  isActive: true,
  isLocalCard: true
}));