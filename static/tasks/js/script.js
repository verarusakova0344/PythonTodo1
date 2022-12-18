const app = document.querySelector('.app')
const app1 = document.querySelector('.app1')
const cards =document.querySelectorAll('.cards')
const card =document.querySelector('.card')
const save_card = document.querySelector('.save_card')
const save_column = document.querySelector('.save_column')


// удалить все колонки
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('delete_all_btn').addEventListener('click', (e)=>{
        document.getElementById('delete_column-app').style.display="block"
    })

    document.getElementById('delete_all_col-btn').addEventListener('click', ()=>{
        document.getElementById('delete_column-app').style.display="none"
        app1.remove()
    })

    document.getElementById('exit_delete_all_col-btn').addEventListener('click', (e)=>{
        document.getElementById('delete_column-app').style.display="none"
    })
})
// изменить колонку
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('column_nav_1_change_btn').addEventListener('click', (e)=>{
        const edit_column_app= document.querySelector('.edit_column_app')
        edit_column_app.style.display="block"
    })

    document.getElementById('exit_edit_col-btn').addEventListener('click', (e)=>{
        document.getElementById('edit_column-app').style.display="none"
    })
})
// удалить колонку
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('column_nav_delete_btn').addEventListener('click', (e)=>{
        document.getElementById('delete_column-app3').style.display="block"
    })

    const column=document.querySelector('.column')
     document.getElementById('delete_col-btn').addEventListener('click', ()=>{
        document.getElementById('delete_column-app3').style.display="none"
        column.remove()
    })


    document.getElementById('exit_delete_col-btn').addEventListener('click', (e)=>{
        document.getElementById('delete_column-app3').style.display="none"
    })
})


// удалить все карточки в столбце
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('column_nav1_delete_btn').addEventListener('click', (e)=>{
        document.getElementById('delete_card-app9').style.display="block"
    })

     document.getElementById('delete_all_card-btn').addEventListener('click', ()=>{
        document.getElementById('delete_card-app9').style.display="none"
        cards.remove()
    })

    document.getElementById('exit_delete_all_card-btn').addEventListener('click', (e)=>{
        document.getElementById('delete_card-app9').style.display="none"
    })
})
// изменить карточку
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('card_nav_change_btn').addEventListener('click', (e)=>{
        document.getElementById('edit_card-app').style.display="block"
    })

    document.getElementById('edit_exit_card-btn').addEventListener('click', (e)=>{
        document.getElementById('edit_card-app').style.display="none"
    })
})
// удалить карточку
document.addEventListener('DOMContentLoaded', (e)=>{
    document.getElementById('card_nav_delete_btn').addEventListener('click', (e)=>{
        document.getElementById('delete_card-app6').style.display="block"
    })

    document.getElementById('delete_card-btn').addEventListener('click', ()=>{
        document.getElementById('delete_card-app6').style.display="none"
        card.remove()
    })

    document.getElementById('exit_delete_card-btn').addEventListener('click', (e)=>{
        document.getElementById('delete_card-app6').style.display="none"
    })
})

let draggedItem = null

function dragNdrop(){

    for (let i=0; i<card.length; i++){
        const item=card[i]

        item.addEventListener('dragstart', () => {
            draggedItem = item
            setTimeout(()=>{
                item.style.display ='none'
            }, 0)
        })
        item.addEventListener('dragend', ()=>{
            setTimeout(()=>{
                item.style.display ='block'
                draggedItem = null
            },0)
        })

        // item.addEventListener ('dblclick', () =>{
        //     item.remove()
        // })

        for (let j=0; j<cards.length; j++){
            const list=cards[j]

            list.addEventListener('dragover', e => e.preventDefault())

            list.addEventListener('dragenter', function (e){
                e.preventDefault()
                this.style.backgroundColor = 'rgba(0, 0, 0, .2)'
            })

            list.addEventListener('dragleave', function (e){
                this.style.backgroundColor = 'rgba(0, 0, 0, 0)'
            } )

            list.addEventListener('drop', function(e) {
                this.style.backgroundColor = 'rgba(0, 0, 0, 0)'
                this.append(draggedItem)
            })

        }
    }
}
dragNdrop()