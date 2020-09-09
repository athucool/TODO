var app = new Vue({
    el:"#app",
    data: {
        text: '',
        checked: true,
        comment : null, 
        comments : [] ,
        p : false  
    },
    methods : {
        onSubmit()
        {
            let new_comment = this.comment;
            console.log(this.comment);
            if (new_comment == null){
                alert("please fill some content in box")
            }
            else{
                this.comments.push(new_comment);
                this.p = true
            }
           
            this.comment=null;
        }
    }
     
})