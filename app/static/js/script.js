$(function(){
	function show_sources(sources){
		var data_html = '';

		sources.map(data => {
			var html = `
				<a href="${data.uri}">${data.uri}</a> | ${data.last_seen_on}
				<br/>
			`;
			data_html += html;
		});
		return data_html;
	}
	$('#form-search').submit(function(event){
		event.preventDefault();
		var section_hibp_page = $('#hibp-page');
		// var section_hibp_page_display = $('.hibp-page-display');
		section_hibp_page.html('');

		var keyword = $('#input-search').val();
		const newLocal = /^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$/;
		if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(keyword)){
			$.ajax({
			   url: '/api/search?keyword=' + keyword,
			   error: function() {
			      alert("error")
			   },
			   success: function(data) {
				// section_hibp_page_display.show();
				   var data_hibp = data.hibp_mail;

				//    var data_html = '';
				   data_hibp.map(data => {
						var html = `
							<div class="card card-fluid hibp-page-display MuiPaper-elevation8">
								<div class="card-body">
									<div class="row">
										<div class="col-sm-2">
											<img class="pwnLogo large" style="height: 50px;" src="${data.LogoPath}"/>
										</div>
										<div class="col-sm-10">
											<p>
												<span class="pwnedCompanyTitle">${data.Title}</span>
												${data.Description}
											</p>
											<p class="dataClasses">
											<strong>Compromised data:</strong> ${data.DataClasses}
											</p>
										</div>
									</div>  
								</div>
							</div>
							<hr>
						`;
						section_hibp_page.append(html);
				   });
			   },
			   type: 'GET'
			});
		}else if(newLocal.test(keyword)){
			$.ajax({
				url: '/api/search?keyword=' + keyword,
				error: function() {
				   alert("error")
				},
				success: function(data) {
					var data_domain = data.domain_email;
					data_domain.map(data => {
						 var html = `
							<div class="card card-fluid hibp-page-display MuiPaper-elevation8">
								<div class="card-header">
									<a class="card-link" style="color: white;" data-toggle="collapse" href="#id-${data.first_name}">
										${data.value} | ${data.sources.length}
									</a>
								</div>
								<div id="id-${data.first_name}" class="collapse" data-parent="#hibp-page">
									<div class="card-body">
										<p>
											<strong>First Name: </strong> ${data.first_name != null ? data.first_name : ''}
											<br/>
											<strong>Last Name: </strong> ${data.last_name != null ? data.last_name : ''}
											<br/>
											<strong>Phone Number: </strong> ${data.phone_number != null ? data.phone_number : ''}
											<br/>
											<strong>linkedin: </strong> ${data.linkedin != null ? data.linkedin : ''}
										</p>
										<hr>
										${show_sources(data.sources)}
									</div>
								</div>
							</div>
							 <hr>
						 `;
						 section_hibp_page.append(html);
					});
				},
				type: 'GET'
			 });
		}
		
	});
});