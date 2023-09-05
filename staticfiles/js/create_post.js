let select_photo_btn = document.getElementById('select-photo-btn')
let photo_input = document.getElementById('id_photo')
let displayedImage = document.getElementById('display-image')
let photo_display = document.getElementById('photo-display')

select_photo_btn.addEventListener('click', ()=> {
    photo_input.click()
})

photo_input.addEventListener('change', (event)=>{
    const selectedImage = event.target.files[0];
    if (selectedImage) {
        const imageUrl = URL.createObjectURL(selectedImage);
        displayedImage.src = imageUrl;
        photo_display.style.display = 'inline-block'
    }
    
})