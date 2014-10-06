function read(qrCode)
{
	var URL = qrCode;
	console.log(qrCode);

	document.location.href = URL;
}
    
qrcode.callback = read;