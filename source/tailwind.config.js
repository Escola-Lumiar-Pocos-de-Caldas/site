module.exports = {
  content: ['./page.html'],
  theme: {
    extend: {
      colors: {
        navy: {
          950: '#0C1526',
          900: '#12203A',
          800: '#1A2A44',
          700: '#24395C',
          600: '#33507D',
        },
        sun: {
          400: '#F5B041',
          500: '#F39C12',
          600: '#E67E22',
          700: '#CA6A16',
        },
        lumiar: '#FFC132',
        leaf: {
          400: '#2ECC71',
          500: '#27AE60',
          600: '#1E8449',
        },
        cream: {
          50: '#FFFCF6',
          100: '#FDF5E6',
          200: '#F6EAD5',
        },
        graphite: '#2C3E50',
      },
      fontFamily: {
        sans: ['Malva', 'Lato', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'],
      },
      // A escala padrão do Tailwind só vai de 5 em 5; estes passos intermediários
      // são usados no design system (véus sutis sobre navy/branco).
      opacity: {
        6: '0.06',
        8: '0.08',
        12: '0.12',
        18: '0.18',
        72: '0.72',
      },
      borderRadius: {
        card: '20px',
        pill: '999px',
      },
      boxShadow: {
        soft: '0 10px 30px rgba(26,42,68,0.06)',
        lift: '0 18px 45px rgba(26,42,68,0.12)',
        cta: '0 12px 28px rgba(230,126,34,0.35)',
      },
      maxWidth: {
        content: '1180px',
      },
      keyframes: {
        floaty: {
          '0%,100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-14px)' },
        },
        pulseRing: {
          '0%': { transform: 'scale(0.9)', opacity: '0.7' },
          '70%': { transform: 'scale(1.6)', opacity: '0' },
          '100%': { transform: 'scale(1.6)', opacity: '0' },
        },
        marquee: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
      },
      animation: {
        floaty: 'floaty 7s ease-in-out infinite',
        pulseRing: 'pulseRing 2.4s cubic-bezier(0.4,0,0.6,1) infinite',
        marquee: 'marquee 32s linear infinite',
      },
    },
  },
  plugins: [],
};
