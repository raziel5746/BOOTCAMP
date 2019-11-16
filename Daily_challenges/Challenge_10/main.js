let beers = parseInt(prompt("Choose a number of beers"));



for (let i = 1; beers > i; i++) {


    console.log(beers + " bottles of beer on the wall\n" + beers + " bottles of beer\nTake " + i + " down, pass it arround\n" + (beers - i) + " bottles of beer on the wall");

    beers -= i;

    
}