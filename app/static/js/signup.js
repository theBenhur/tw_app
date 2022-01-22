function signUp(e){
    e.preventDefault()
    const username=document.getElementById('username').value
    const password=document.getElementById('password').value
    const email=document.getElementById('email').value
    const language=document.getElementById('language').value
    const plan=document.getElementById('plan').value
    if(username.length && password.length && email.length && language.length && plan.length){
        const body=JSON.stringify({
            username,password,email,language,plan
        })
        const url=e.target.action
        fetch(url,{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body
        })
        .then(async response=>{
            return {
                status:response.status,
                ...await response.json()
            }
        })
        .then(response=>{
            if(response.status == 201){
                alert(response.message)
                window.location.href='/'
            }
            if(response.status == 200){
                alert(response.message)
            }
        })
    }else{
        alert('You most have to fill all fields')
    }

}
document.forms[0].addEventListener('submit',e=>signUp(e))
// function enableRepeatPassword(){
//     if(password.value.length) repeat_password.disabled=false
//     else repeat_password.disabled=true
// }
// function enableSubmitButton(){
//     let equals=password.value === repeat_password.value?false:true
//     if(equals) matched_passwords.innerHTML='The passwords does not match'
//     submit_button.disabled=equals
// }

// $(document).ready(function(){
//     let valid_username=false
//     let valid_password=false
//     $('#username').on('keyup',function(){
//         let username=$('#username').val()
//         if(username.length){
//             fetch(`/users/${username}`,{method:'GET'})
//             .then(async response => {
//                 return {
//                     status:response.status,
//                     ...await response.json()
//                 }
//             })
//             .then(response =>{
//                 if(response.status == 200){
//                     $('#exists-user').removeClass('bg-success')
//                     $('#exists-user').addClass('bg-danger')
//                     $('#exists-user').html(`${response.message}`)
//                     valid_username=false
//                 }
//                 if(response.status == 404){
//                     $('#exists-user').removeClass('bg-danger')
//                     $('#exists-user').addClass('bg-success')
//                     $('#exists-user').html(`${response.message}`)
//                     valid_username=true
//                     if(valid_password) $('#sign-up').prop('disabled',false)
//                 }
//             })
//         }else{
//             $('#exists-user').removeClass('bg-danger')
//             $('#exists-user').removeClass('bg-success')
//             $('#exists-user').html('')
//             valid_username=false
//         }
//     })
//     $('#password').on('keyup',function(){
//         if($(this).val().length) $('#repeat_password').prop('disabled',false)
//         else $('#repeat_password').prop('disabled',true)
//     })
//     $('#repeat_password').on('keyup',function(){
//         console.log($(this).val() != $('#password').val())
//         if($(this).val() != $('#password').val()){
//             $('#matched_passwords').html('The passwords does not match')
//             $('#matched_passwords').removeClass('bg-success')
//             $('#matched_passwords').addClass('bg-danger')
//             $('#sign-up').prop('disabled',false)
//         }else{
//             $('#matched_passwords').html('The passwords matched')
//             $('#matched_passwords').removeClass('bg-danger')
//             $('#matched_passwords').addClass('bg-success')
//             if(valid_username) $('#sign-up').prop('disabled',false)
//         }
//     })
// })