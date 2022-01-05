function verify_fields(username,password){
    return username.length>0 && password.length>0
}
function login(e){
    e.preventDefault()
    const username=document.querySelector('input[name="username"]').value
    const password=document.querySelector('input[name="password"]').value
    const body=JSON.stringify({
        username,
        password
    })
    const url=e.target.action

    if(!verify_fields(username,password)){
        alert('You must provide all the fields')
        return 
    }
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body
    })
    .then( async response=>{
        return {
            status:response.status,
            ...await response.json()
        }
    })
    .then(response => {
        if(response.status == 404){
            const wrong_crendetials=document.getElementById("wrong_credentials")
            wrong_crendetials.innerHTML=`<p class="danger">${response.message}</p>`
        }
    })
    .catch(err => {
        console.log(err)
    })
}

document.forms[0].addEventListener('submit',(e)=>login(e))