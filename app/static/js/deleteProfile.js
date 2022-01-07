function deleteProfile(e){
    e.preventDefault()
    const url=document.getElementById('delete_profile').parentNode.href
    fetch(url,{method:'DELETE'})
    .then(async response=>{
        return {
            status:response.status,
            ...await response.json()
        }
    })
    .then(response=>{
        if(response.status == 200){
            alert(response.message)
            window.location.href='/home'
        }
    })
}

document.getElementById('delete_profile').addEventListener('click',e=>deleteProfile(e))
