module.exports = {
    
    "transpileDependencies": [
        "vuetify"
    ],
    outputDir: 'dist',
    assetsDir: 'static',
    // baseUrl: 'localhost:8000/static/',
    // baseUrl: IS_PRODUCTION
    // ? 'http://cdn123.com'
    // : '/',
    // For Production, replace set baseUrl to CDN
    // And set the CDN origin to `yourdomain.com/static`
    // Whitenoise will serve once to CDN which will then cache
    // and distribute
    devServer: {
        proxy: {
            // '/*': {
            '/api': {
                // Forward frontend dev server request for /api to django dev server
                target: 'https://markanthonyvale.herokuapp.com/',
                // target: 'http://localhost:8000/',
            },
        }
    }
}
// {
    
// }