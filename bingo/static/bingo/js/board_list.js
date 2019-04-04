$(document).ready(function(){
  $('input[type="text"], input[type="password"]').addClass('form-control').prev().addClass('sr-only').parent().addClass('form-group mr-4')
  var imgs = $('img.thumbnail');
  imgs.bind('mouseover', function(){this.src = this.src.replace("voted", "marked")});
  imgs.bind('mouseout', function(){this.src = this.src.replace("marked", "voted")});
});
