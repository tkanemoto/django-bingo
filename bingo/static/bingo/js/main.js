$(document).ready(function(){
    var imgs = $('img.thumbnail');
    imgs.bind('mouseover', function(){console.log(this.src);this.src = this.src.replace("voted", "marked")});
    imgs.bind('mouseout', function(){this.src = this.src.replace("marked", "voted")});
});
$(document).ready(function(){
    var imgs = $('img.thumbnail');
    imgs.bind('mouseover', function(){console.log(this.src);this.src = this.src.replace("voted", "marked")});
    imgs.bind('mouseout', function(){this.src = this.src.replace("marked", "voted")});
});
