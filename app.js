const canvas = require('canvas');
const fs = require('fs');

function run(text){
    const h = 580;
    const w = 340;
    const canv = canvas.createCanvas(w, h);
    const ctx = canv.getContext('2d');

    ctx.fillStyle = '#009900';
    ctx.fillRect(0,0, w, h);

    ctx.fillStyle = '#000000';
    ctx.textAlign = 'center';
    ctx.font = '40px Arial'
    ctx.fillText(text, w / 2, h / 2);

    const stream = canv.createPNGStream();
    const out = fs.createWriteStream(`./images/${text}.png`);

    stream.pipe(out);

}
function start(){
    for(var i = 1; i <= 64; i++){
        // run(i);
    }
}

// start();

function start2(){
    let files = fs.readdirSync('./images');
    files.sort(_=> Math.random() - 0.5);
    let arr = files.slice(0, 64);
    let arr2 = arr.reduce((acc, item) =>{
        let [name, ext] = item.split('.');
        acc.push({
            path : `./images/${item}`,
            name
        });
        return acc;
    }, []);
    console.log(arr2);
}
start2();