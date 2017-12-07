//where we will call our ajax function
$(document).ready(function() {
	$('form').submit(function(event) {
		event.preventDefault()
		form = $("form")

		$.ajax({
			'url':'/ajax/newsletter',//url as the urlconf 
			'type':'POST',//type of request
			'data':form.serialize(),//serialize function converts the form values into a JSON that can be passed into the request 
			'dataType':'json',
			'success':function(data) {
				alert(data['success'])
			},
			})//end of ajax method
			$('#id_your_name').val('')
			$('#id_email').val(''
	})//end of submit event
})