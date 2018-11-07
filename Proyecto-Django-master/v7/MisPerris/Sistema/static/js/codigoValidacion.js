$(function(){
   //sacar los mensajes de error
	 $("erroremail").hide();
	 $("errorRutPostulante").hide(); 
	 $("errorNombreCompleto").hide();
	 $("errorFechaNacimiento").hide();
    //variables que indican valor de estado validacion  
	var error_email = false;
	var error_rut_postulante = false;
	var error_nombre_completo = false;
	var error_fecha_nacimiento = false;
	$("#email").focusout(function() {

	//		check_email();
		
	});
	
	$("#rutPostulante").focusout(function() {

			//validaRut();
		
	});
	$("#nombreCompleto").focusout(function() {

			//validaNombreCompleto();
		
	});
	
	$("#fechaNacimiento").focusout(function() {

			//validaFechaNacimiento();
		
	});
	
	
	function check_email() {

		var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
	
		if(pattern.test($("#email").val())) {
			$("#erroremail").hide();
		} else {
			$("#erroremail").html("Direccion inválida");
			$("#erroremail").show();
			error_email = true;
		}
	
	}
	
	//validacion Rut
	function validaRut(){
		
		if ($("#rutPostulante").length == 0  ){
			$("#errorRutPostulante").html("Rut Invalido");
			$("#errorRutPostulante").show();
			error_rut_postulante = true;
		}
		if ( $("#rutPostulante").length < 10 ){ 
			$("#errorRutPostulante").html("Rut Invalido");
			$("#errorRutPostulante").show();
			error_rut_postulante = true; }
		else{
			$("#errorRutPostulante").hide();
		}
		
		var pattern = new RegExp(/^\d{7,8}-[k|K|\d]{1}$/);
	
		if(pattern.test($("#rutPostulante").val())) {
			$("#errorRutPostulante").hide();
		} else {
			$("#errorRutPostulante").html("Rut inválida");
			$("#errorRutPostulante").show();
			error_rut_postulante = true;
		}
	}
	//validacion Nombre Completo
	function validaNombreCompleto() {
		var pattern = new RegExp(/^[+a-zA-Z]/);
		if(pattern.test($("#nombreCompleto").val())) {
			$("#errorNombreCompleto").hide();
		} else {
			$("#errorNombreCompleto").html("Caracteres Invalidos");
			$("#errorNombreCompleto").show();
			error_nombre_completo = true;
		}
	
	}	
	
	
	function validaFechaNacimiento(){
		
		if($("#fechaNacimiento").getFullYear() > 2001){
			$("#errorFechaNacimiento").hide();
		}else{
			$("#errorFechaNacimiento").html("Fecha invalida");
			$("#errorFechaNacimiento").show();
			error_fecha_nacimiento = true;
		}
	}
	
	$("#registration_form").submit(function() {
											
		
		error_email = false;
		error_rut_postulante = false;
		error_nombre_completo = false;	
		/*error_fecha_nacimiento =false;*/
	
		check_email();
		validaRut();
		validaNombreCompleto();
		/*validaFechaNacimiento();*/
		
		if(error_email == false && validaRut == false && validaNombreCompleto == false) {
			return true;
		} else {
			return false;	
		}

});
});