function create(e){
    e.preventDefault()
    formData=new FormData()
    formData.append('profilename',document.getElementById('profilename').value)
    formData.append('language',document.getElementById('language').value)
    formData.append('image',document.querySelector('input[name="image"]').files[0])

    url=e.target.action
    fetch(url,{
        method:'POST',
        body:formData
    })
    .then(async response=>{
        return {
            status:response.status,
            ...await response.json()
        }
    })
    .then(response=>{
        if(response.status == 201) alert(response.message)
        if(response.status == 200) alert(response.message)
    })
}

document.forms[0].addEventListener('submit',e=>create(e))