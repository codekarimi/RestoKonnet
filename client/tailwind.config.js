/** @type {import('tailwindcss').Config} */

module.exports = {
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    theme: {
        extend: {
            colors: {
                ryellow: '#FFAA29',
                rgreen: {
                    100: '#489B53',
                    200: '#306737',
                }
            },
        },
    },
    variants: {
        extend: {},
    },
    content: [
        './node_modules/preline/preline.js',
    ],
    
    plugins: [
        require('preline/plugin'),
    ],
}