


// редактировать карточку
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('column_nav_1_change_btn').addEventListener('click', (e)=>{
        document.getElementById('edit_card').style.display="block"
    })

    document.getElementById('save_card_edit-btn').addEventListener('click', (e)=>{
        document.getElementById('edit_card').style.display="none"
    })

    document.getElementById('exit_card_edit-btn').addEventListener('click', (e)=>{
        document.getElementById('edit_card').style.display="none"
    })

})
// удалить карточку
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('column_nav_1_delete').addEventListener('click', (e)=>{
        document.getElementById('delete_card').style.display="block"
    })

    document.getElementById('delete_card-btn').addEventListener('click', (e)=>{
        document.getElementById('delete_card').style.display="none"
        document.getElementById('cards').remove()
    })

    document.getElementById('exit_delete_card-btn').addEventListener('click', (e)=>{
        document.getElementById('delete_card').style.display="none"
    })

})

//добавить и удалить пользователя

document.addEventListener('DOMContentLoaded', (e)=>{

    function addUser(){
        const app22 = document.querySelector('.app22')
        const newToCard = document.createElement('div')
        newToCard.classList.add('cards_2')
        newToCard.innerHTML=` 
        <div class="guest_cards">
            <div class="guest_cards_1">
                <div class="cards_item">Название Доски</div>
            </div>

    </div>`

        app22.append(newToCard)
        document.getElementById('add_to_card').style.display="none"

    }
    document.getElementById('save_add_to_card-btn').addEventListener('click', addUser)


    function deleteUser(){
        const app22 = document.querySelector('.app22')
        const newToCard = document.createElement('div')
        newToCard.classList.add('cards_2')
        newToCard.innerHTML=` 
        <div class="guest_cards">
            <div class="guest_cards_1">
                <div class="cards_item">Название Доски</div>
            </div>

    </div>`

        app22.append(newToCard)
        document.getElementById('add_to_card').style.display="none"

    }
    document.getElementById('save_add_to_card-btn').addEventListener('click', deleteUser)

})