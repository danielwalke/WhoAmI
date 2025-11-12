const isSecure = window.location.protocol === 'https:';
const wsProtocol = isSecure ? 'wss' : 'ws';
export const SERVER_URL = window.location.hostname === 'localhost' ? 'http://localhost:8000' : 'https://daniel-walke.com'
export const CLIENT_URL = window.location.hostname === 'localhost' ? 'http://localhost:5173' : 'https://daniel-walke.com'
export const SERVER_PREFIX = 'whoami'
export const WEBSOCKET_URL = window.location.hostname === 'localhost' ? `ws://localhost:8000/${SERVER_PREFIX}/ws` : `${wsProtocol}://daniel-walke.com/${SERVER_PREFIX}/ws`