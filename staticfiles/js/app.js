
let menu = document.querySelector('.menu')
let category_btn = document.querySelector('.categories-wrapper')
let content_menu = document.querySelector('.menu-content')
let dropdown_content = document.querySelector('.on-mobile')
let main_menu = document.querySelector('.main-menu')
let cancel = document.querySelector('.cancel')
let dotted_menu_content = document.querySelectorAll('.dotted_menu_content')

menu.addEventListener("click", ()=> {
    main_menu.classList.toggle('main-menu-toggle')
    cancel.classList.toggle('cancel-toggle')
    content_menu.classList.toggle('menu-content-added')
   
})

category_btn.addEventListener("click", ()=> {
    console.log('hello')
    dropdown_content.classList.toggle('clicked')
})




