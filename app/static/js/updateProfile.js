function update(e){
    e.preventDefault()
    formData=new FormData()
    formData.append('profilename',document.getElementById('profilename').value)
    formData.append('language',document.getElementById('language').value)
    formData.append('image',document.querySelector('input[name="image"]').files[0])
    const url=e.target.action
    fetch(url,{
        method:'POST',
        // headers:{'Content-Type':'application/json'},
        body:formData
    })
    .then(async response=>{
        console.log(response)
        return {
            status:response.status,
            ...await response.json()
        }
    })
    .then(response=>{
        if(response.status == 203){
            alert(response.message)
            window.location.reload()
        }
        if(response.status == 501){
            alert(response.message)
            profilename.focus()
        }

    })
}

document.forms[0].addEventListener('submit',e=>update(e))