function clearComment(){
	$('#txt1').val('');
	$('#namebox').val('Name');
}


function saveComment()
{
var ctext = $('#txt1').val();
var cname = $('#namebox').val();
if (cname === 'Name'){cname = 'Anon';}
//alert('saveComment cname=' + dffddff + ' ctext=' + ctext);

var comments = cname + ':' + ctext + '<br>' + '<br>';
$('#cmtlist9').prepend(comments);


var prevComments = $('#cmtlist9').html();


setObject('key', prevComments);

$('#txt1').val('');
$('#namebox').val('Name');
}

// Hide the extra content initially, using JS so that if JS is disabled, no problemo:
$('.read-more-content').addClass('hide')
$('.read-more-show, .read-more-hide').removeClass('hide')

// Set up the toggle effect:
$('.read-more-show').on('click', function(e) {
  $(this).next('.read-more-content').removeClass('hide');
  $(this).addClass('hide');
  e.preventDefault();
});

// Changes contributed by @diego-rzg
$('.read-more-hide').on('click', function(e) {
  var p = $(this).parent('.read-more-content');
  p.addClass('hide');
  p.prev('.read-more-show').removeClass('hide'); // Hide only the preceding "Read More"
  e.preventDefault();
});

