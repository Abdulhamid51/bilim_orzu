$message = $('.messages_pro')
$success = '<h5 class="text-success">Tasdiqlandi!</h5>'
$danger = '<h5 class="text-danger">Tastiqlanmadi!!!</h5>'

$('.com_submit').on('click', function(){
    $com = $('.com_body').val();
    $name = $('.com_name').val();
    $surname = $('.com_surname').val();
    $news_id = $('.news_id').data('id')

    $base = $('.commments')

    $.ajax({
        url:'/comment/',
        type:'GET',
        data:{
            'id':$news_id,
            'name':$name,
            'surname':$surname,
            'comment':$com
        },
        success:function(response){
            
            if(response['status']==='OK'){
                $message.append($success)
                $base.prepend(`
                    <li class="comment rounded">
                        <div class="thumb">
                            <img src="/static/images/other/comment-1.png" alt="John Doe" />
                        </div>
                        <div class="details">
                            <h4 class="name"><a href="#">${response['name']} ${response['surname']}</a></h4>
                            <span class="date">${response['date']}</span>
                            <p>${response['comment']}</p>
                        </div>
                    </li>
                `)
            }else{
                $message.append($danger)
            }
        }
    })
})

$('a#submit').on('click', function(){
    
    $name = $('#InputName').val()
    $surname = $('#InputSurname').val()
    $phone = $('#InputPhone').val()
    $.ajax({
        url:'/jamoa/boglan/',
        type:'GET',
        data:{
            'name':$name,
            'surname':$surname,
            'phone':$phone
        },
        success:function(response){
            if(response['status']==='OK'){
                $message.append($success)
            }else{
                $message.append($danger)
            }
        }
    })
})