(_=>{
    let a = [];
    for(var i = 1 ; i <= 64 ;i++){
        a.push({
            path : `./images/${i}.png`,
            name : i
        });
    }
    console.log(a);
})();