const audio = document.querySelector("audio"); 

// Adding custom play/pause buttons 
const playButton = document.getElementbyId("play-button"); 
const pauseButton = document.getElementbyId("pause-button"); 

playButton.addEventListener("click",() => {
    audio.play(); 
}); 

pauseButton.addEventListener("click", ()=> {
    audio.pause(); 
}); 