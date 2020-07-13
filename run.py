from app import create_app
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(".ssl/projectcti_com.ca-bundle")
context.load_cert_chain(".ssl/projectcti_com.crt", ".ssl/key.pem")

if __name__ == "__main__":
	app = create_app('settings')
	# app.run(host="0.0.0.0", port=5000, debug=True)
	app.run(host="0.0.0.0", port=5000, ssl_context=context)