function handleNavbar() {
    categories_block.classList.remove('block')   
}

window.addEventListener('scroll', handleNavbar)

let categories_block = document.querySelector('.categories-block')
let categories_over = document.querySelector('.categories')
let categories_leave = document.querySelector('.categories')

categories_over.addEventListener('mouseover', handleCategoriesMouseover)
// categories_leave.addEventListener('mouseleave', handleCategoriesMouseover)
let body = document.querySelector('body')

function handleCategoriesMouseover() {
    categories_block.classList.toggle('block')   
}


body.addEventListener('click', ()=>{
    categories_block.classList.remove('block')
})

