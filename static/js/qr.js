function read(qrCode)
{
	var URL = "/account/" + qrCode;
	console.log(qrCode);

	document.location.href = URL;
}
    
qrcode.callback = read;