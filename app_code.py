# -*- coding: utf-8 -*-
APP_CODE = r"""
const { useState, useEffect, useRef } = React;

// Leaflet's bindTooltip/divIcon render string content as raw HTML (no auto-escaping,
// unlike React). Any user-entered text (city names, activity names) reaching those
// APIs must be escaped here first to prevent stored XSS via a saved trip or a
// shared read-only trip link.
function escapeHtml(str) {
  if (str == null) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/* ---------- minimal inline icons ---------- */
function IconBase({ size = 16, style, children }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor"
      strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={style}>
      {children}
    </svg>
  );
}
const ArrowLeft = (p) => <IconBase {...p}><path d="M19 12H5" /><path d="M12 19l-7-7 7-7" /></IconBase>;
const ChevronRight = (p) => <IconBase {...p}><path d="M9 18l6-6-6-6" /></IconBase>;
const Users = (p) => <IconBase {...p}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></IconBase>;
const Languages = (p) => <IconBase {...p}><path d="M5 8l6 6" /><path d="M4 14l6-6 2-3" /><path d="M2 5h12" /><path d="M7 2h1" /><path d="M22 22l-5-10-5 10" /><path d="M14 18h6" /></IconBase>;
const Coins = (p) => <IconBase {...p}><circle cx="8" cy="8" r="6" /><path d="M18.09 10.37A6 6 0 1 1 10.34 18" /><path d="M7 6h1v4" /><path d="M16.71 13.88l.7.71-2.82 2.82" /></IconBase>;
const CalendarClock = (p) => <IconBase {...p}><path d="M21 7.5V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h6" /><path d="M16 2v4" /><path d="M8 2v4" /><path d="M3 10h18" /><circle cx="18" cy="18" r="4" /><path d="M18 16.5v1.5l1 1" /></IconBase>;
const Compass = (p) => <IconBase {...p}><circle cx="12" cy="12" r="10" /><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76" /></IconBase>;
const ImageOff = (p) => <IconBase {...p}><path d="M3 3l18 18" /><path d="M21 15V5a2 2 0 0 0-2-2H9" /><path d="M3 8v11a2 2 0 0 0 2 2h13" /><circle cx="9" cy="9" r="1.5" /></IconBase>;
const ShieldCheck = (p) => <IconBase {...p}><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" /><path d="M9 12l2 2 4-4" /></IconBase>;
const Utensils = (p) => <IconBase {...p}><path d="M3 2v7a2 2 0 0 0 2 2h0a2 2 0 0 0 2-2V2" /><path d="M5 11v11" /><path d="M19 2v20" /><path d="M15 2v7a2 2 0 0 0 4 0V2" /></IconBase>;
const MapPinIcon = (p) => <IconBase {...p}><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z" /><circle cx="12" cy="10" r="3" /></IconBase>;
const Search = (p) => <IconBase {...p}><circle cx="11" cy="11" r="8" /><path d="M21 21l-4.35-4.35" /></IconBase>;
const X = (p) => <IconBase {...p}><path d="M18 6L6 18" /><path d="M6 6l12 12" /></IconBase>;
const Award = (p) => <IconBase {...p}><circle cx="12" cy="8" r="6" /><path d="M8.21 13.89L7 23l5-3 5 3-1.21-9.12" /></IconBase>;
const Copy = (p) => <IconBase {...p}><rect x="9" y="9" width="13" height="13" rx="2" /><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" /></IconBase>;
const UserIcon = (p) => <IconBase {...p}><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></IconBase>;
const CheckCircle = (p) => <IconBase {...p}><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" /><path d="M22 4L12 14.01l-3-3" /></IconBase>;
const StarIcon = (p) => <IconBase {...p}><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></IconBase>;
const LogOutIcon = (p) => <IconBase {...p}><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" /><path d="M16 17l5-5-5-5" /><path d="M21 12H9" /></IconBase>;
const PlusIcon = (p) => <IconBase {...p}><path d="M12 5v14" /><path d="M5 12h14" /></IconBase>;
const Download = (p) => <IconBase {...p}><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /><path d="M7 10l5 5 5-5" /><path d="M12 15V3" /></IconBase>;
const HomeIcon = (p) => <IconBase {...p}><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9Z" /><path d="M9 22V12h6v10" /></IconBase>;
const SuitcaseIcon = (p) => <IconBase {...p}><rect x="3" y="7" width="18" height="13" rx="2" /><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" /></IconBase>;
const FileIcon = (p) => <IconBase {...p}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z" /><path d="M14 2v6h6" /></IconBase>;
const BagIcon = (p) => <IconBase {...p}><path d="M6 2h12l1 5H5l1-5Z" /><path d="M4 7h16v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7Z" /></IconBase>;
const MailIcon = (p) => <IconBase {...p}><rect x="2" y="4" width="20" height="16" rx="2" /><path d="M22 6l-10 7L2 6" /></IconBase>;
const MenuIcon = (p) => <IconBase {...p}><path d="M4 6h16M4 12h16M4 18h16" /></IconBase>;
const DollarIcon = (p) => <IconBase {...p}><path d="M12 1v22" /><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" /></IconBase>;
const PlugIcon = (p) => <IconBase {...p}><path d="M9 2v6M15 2v6" /><path d="M6 8h12v4a6 6 0 0 1-12 0V8Z" /><path d="M9 18v3M15 18v3" /></IconBase>;
const PlaneIcon = (p) => <IconBase {...p}><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-3 2v1.5l4.5-1.5 4.5 1.5V21l-3-2v-5.5l8 2.5Z" /></IconBase>;
const RefreshIcon = (p) => <IconBase {...p}><path d="M21 12a9 9 0 0 1-15.5 6.3L3 15" /><path d="M3 12a9 9 0 0 1 15.5-6.3L21 9" /><path d="M3 21v-6h6" /><path d="M21 3v6h-6" /></IconBase>;
const GoogleG = (p) => (
  <svg width={p.size || 16} height={p.size || 16} viewBox="0 0 18 18">
    <path fill="#4285F4" d="M17.64 9.2c0-.64-.06-1.25-.16-1.84H9v3.48h4.84c-.21 1.13-.84 2.09-1.79 2.73v2.27h2.9c1.7-1.56 2.68-3.87 2.68-6.64z" />
    <path fill="#34A853" d="M9 18c2.43 0 4.47-.8 5.96-2.18l-2.9-2.27c-.8.54-1.84.86-3.06.86-2.35 0-4.34-1.59-5.05-3.72H.96v2.34C2.44 15.98 5.48 18 9 18z" />
    <path fill="#FBBC05" d="M3.95 10.69A5.4 5.4 0 0 1 3.66 9c0-.59.1-1.16.29-1.69V4.97H.96A9 9 0 0 0 0 9c0 1.45.35 2.83.96 4.03l2.99-2.34z" />
    <path fill="#EA4335" d="M9 3.58c1.32 0 2.51.45 3.44 1.35l2.58-2.58C13.46.89 11.43 0 9 0 5.48 0 2.44 2.02.96 4.97l2.99 2.34C4.66 5.17 6.65 3.58 9 3.58z" />
  </svg>
);

/* ---------- UI text translations (chrome only; country data is localized separately via .pt fields) ---------- */
const UI_STRINGS = {
  en: {
    home: "Home", articles: "Articles", products: "Products", newsletter: "Newsletter", aboutMe: "About me",
    heroHeadline: "Explore the world, one waypoint at a time.",
    heroTagline: "Everything for your next trip, in one place: real country guides, an interactive map to track where you've been and where you want to go, and a planner to build your itinerary day by day.",
    statsCountries: "countries", statsAttractions: "attractions", statsLanguages: "languages",
    featExploreTitle: "Explore", featExploreDesc: "Real itineraries, costs, and food for every country.",
    featTrackTitle: "Track", featTrackDesc: "Mark where you've been and where you want to go on an interactive map.",
    featPlanTitle: "Plan", featPlanDesc: "Build your next trip day by day, then export it.",
    allContinents: "All continents", countries: "countries", capital: "Capital",
    topAttractions: "Top attractions", suggestedItinerary: "Suggested itinerary", days: "days", day: "day",
    tripEssentials: "Trip essentials", dailyBudget: "Daily budget", visa: "Visa",
    plugVoltage: "Plug & voltage", tipping: "Tipping", safety: "Safety", gettingAround: "Getting around",
    gettingThere: "Getting there", cost: "Cost", eat: "Where to eat", faqTitle: "Frequently asked questions",
    population: "Population", language: "Language", currency: "Currency", bestTime: "Best time to visit",
    tastesOf: "Tastes of", pairsWith: "Pairs well with", bookAhead: "Book ahead",
    searchHome: "Search for a country...", searchContinent: "Search countries in this continent...",
    noResultsFor: "No countries found for", inContinent: "in",
    whereToGoNow: "Where to go now", whereToGoNowSubtitle: "A few ideas worth booking this month, updated every month.",
    monthlyEyebrow: "Updated monthly",
    quizTitle: "This month's Passport Quiz", quizSubtitle: "8 questions. How many countries can you get right?",
    quizStart: "Start quiz", quizQuestionLabel: "Question", quizOf: "of",
    quizPromptTagline: "Which country is this?", quizPromptHighlight: "Which country is famous for this?",
    quizPromptFood: "Which country is this dish from?", quizPromptFlag: "Which country does this flag belong to?",
    quizNext: "Next question", quizSeeResults: "See results",
    quizYourScore: "Your score", quizPlayAgain: "Play again",
    quizCopyResult: "Copy your result", quizCopied: "Copied to clipboard!",
    quizShareText: "I scored SCORE/8 on Waypoint's Passport Quiz this month 🧳 Can you beat me?",
    quizRank0: "Just got the passport", quizRank1: "Frequent flyer", quizRank2: "World wanderer", quizRank3: "Waypoint Master",
    signIn: "Sign in", signOut: "Sign out", createAccount: "Create account",
    continueWithGoogle: "Continue with Google", orDivider: "or",
    emailLabel: "Email", passwordLabel: "Password",
    authSubmitSignIn: "Sign in", authSubmitSignUp: "Create account",
    authSwitchToSignUp: "Don't have an account? Create one", authSwitchToSignIn: "Already have an account? Sign in",
    nudgeTitle: "Welcome to Waypoint!", nudgeSubtitle: "Want the newsletter too? Same great trips, straight to your inbox.",
    nudgeSkip: "Maybe later",
    newsletterSubscribeBtn: "Subscribe", newsletterBusy: "Subscribing…",
    newsletterSuccess: "You're in! Watch your inbox for the next issue.",
    newsletterError: "Something went wrong — check the email and try again.",
    authModalTitleIn: "Welcome back", authModalTitleUp: "Create your account",
    authModalSubtitle: "Track which countries you've visited and which you want to see next.",
    markVisited: "Visited", markWantToVisit: "Want to visit",
    signInToTrackHint: "Sign in to track this country",
    myMap: "Map", mapTitle: "Your map", mapSubtitle: "Every country you've marked, all in one place.",
    mapLegendVisited: "Visited", mapLegendWant: "Want to visit", mapLegendNone: "Not marked",
    mapSignInPrompt: "Sign in to start marking countries on your map.",
    mapVisitedListTitle: "Visited", mapWantListTitle: "Want to visit", mapListEmpty: "Nothing here yet.",
    mapLoading: "Loading map…", mapLoadError: "Couldn't load the map. Check your connection and try again.",
    countryDetailLoading: "Loading country details…",
    countryDetailError: "Couldn't load this country's details. Check your connection and try again.", tryAgain: "Try again",
    essentialAnchor: "Essential", placesAnchor: "Places", foodAnchor: "Flavors", routeAnchor: "Itinerary", faqAnchor: "FAQs",
    readMore: "Read more", readLess: "Read less", showMap: "Show map", hideMap: "Hide map",
    pctOfWorldVisited: "of the world visited",
    myTrips: "Trips", tripsSubtitle: "Plan your next trip, day by day.",
    tripsStatTrips: "TRIPS", tripsStatContinents: "CONTINENTS", tripsStatNights: "NIGHTS PLANNED", tripsStatDone: "COMPLETED",
    routeTab: "Route", daysTab: "Days", bookingsTab: "Bookings", comingSoonBadge: "coming soon",
    whereToSleepBtn: "Where to sleep", whereToEatBtn: "Where to eat",
    placesBtn: "Places", placesCountSuffix: "places", transportTitle: "Transport",
    transportModeLabel: "Mode of transport", transportDurationLabel: "Duration", transportCostLabel: "Cost",
    mapIllustrativeLabel: "Illustrative map", mapIllustrativeNote: "Overland route shown, not to scale.",
    transitAddBtn: "Add travel time", transitEditBtn: "Edit",
    highlightsChipLabel: "highlights", doneEditingLabel: "done",
    dayListEmpty: "Nothing planned for this day yet.", dayMapEmpty: "Add a place to this day to see it on the map.",
    openMenu: "Open menu", closeMenu: "Close menu", menuLabel: "MENU", languageLabel: "Language",
    signedInAs: "Signed in as", notSignedIn: "Not signed in — tap to sign in",
    daySuggestionsLabel: "From your highlights — tap to add to this day", suggestionsIn: "Suggestions in",
    pdfCoverTagline: "A slow, ad-free way to explore the world.",
    pdfEssentialsTitle: "Trip essentials", pdfAboutTitle: "About",
    pdfRouteTitle: "Your route", pdfFarewellTitle: "Have a wonderful trip!",
    pdfFarewellLine: "Wherever these days take you, we hope they're unhurried, well-fed, and full of good light.",
    pdfFarewellSign: "— Waypoint", pdfPopulation: "Population", pdfLanguage: "Language", pdfCurrency: "Currency", pdfBestTime: "Best time to visit",
    addActivityPlaceholder: "place or activity name", activityTimePlaceholder: "time",
    listViewLabel: "List", mapViewLabel: "Map",
    bookingsAll: "All", bookingsFlights: "Flights", bookingsHotels: "Hotels",
    flightNumberPlaceholder: "flight number", flightTimePlaceholder: "time", flightRefPlaceholder: "booking reference",
    noFlightsYet: "No flights added yet — set a stop's travel mode to \"Flight\" in Route to add one here.",
    noHotelsYet: "No stays added yet — add one under \"Where to sleep\" in Route.",
    confirmedLabel: "Confirmed", pendingLabel: "Pending",
    documentsTitle: "Documents", addDocumentPlaceholder: "e.g. Passport — no. ABC123, valid until 2029",
    noDocumentsYet: "No documents added yet.", viewInRoute: "View in Route",
    tripsSignInPrompt: "Sign in to start planning a trip.", noTripsYet: "No trips yet — start planning your next one.",
    newTrip: "New trip", tripNameLabel: "name", tripNamePlaceholder: "e.g. Thailand 2027",
    tripCountryLabel: "country", tripDatesLabel: "dates", daysWillBeCreated: "days will be created automatically",
    createTrip: "Create trip", tripStatusPlanning: "planning", tripStatusDone: "done",
    days: "days", stops: "stops", estimatedCost: "estimated cost", perDay: "per day",
    cityPlaceholder: "city or region", day: "day", addHighlightPlaceholder: "add a highlight",
    addStop: "Add stop", chooseTransit: "choose transit", transitFlight: "flight", transitTrain: "train",
    transitBus: "bus", transitCar: "car", transitBoat: "boat", transitDuration: "duration, e.g. 12h",
    transitPrice: "price, e.g. €25", markTripDone: "Mark trip as done", deleteTrip: "Delete trip",
    confirmDeleteTrip: "Delete this trip? This can't be undone.",
    whereToSleep: "Where to sleep", whereToEat: "Where to eat", nights: "nights",
    stayNamePlaceholder: "hotel or place name", nightsPlaceholder: "nights", addMealPlaceholder: "restaurant or dish",
    exportPdf: "Export PDF", typicalRange: "typical range",
    insertStopHere: "insert stop here", hoursLabel: "hours", minutesLabel: "min",
    saveTrip: "Save", tripSaved: "Saved",
    dayNotes: "Day notes", dayNotesPlaceholder: "How did the day go? Anything to remember...",
    dayNotesSubtitle: "A running journal for the trip, one line per day.", addNoteForDay: "+ Add a note for this day",
    shareTrip: "Share trip",
    shareTripOnDesc: "Anyone with the link can view this trip (read-only).",
    shareTripOffDesc: "Make this trip public to share a read-only link.",
    copyLink: "Copy link", linkCopied: "Link copied",
    sharedTripBanner: "You're viewing a shared trip — read-only",
    sharedTripNotFound: "This trip isn't available. The link may be wrong, or sharing was turned off.",
    sharedTripLoading: "Loading trip…",
    planYourOwnTrip: "Plan your own trip on Waypoint", backToWaypoint: "Back to Waypoint",
    articlesComingSoon: "Long-form guides, itineraries, and travel notes are on their way — check back soon.",
    productsComingSoon: "Downloadable guides, packing lists, and planning tools are on their way — check back soon.",
    newsletterIntro: "Get a new destination in your inbox every week — real itinerary ideas and travel notes, no spam.",
    footerTagline: "A slow, ad-free way to explore the world, one country at a time.",
    footerExplore: "Explore", footerConnect: "Connect", footerProjectBy: "A project by",
    footerBuiltFor: "Built for people who plan their trips a little too carefully.",
  },
  pt: {
    home: "Início", articles: "Artigos", products: "Produtos", newsletter: "Newsletter", aboutMe: "Sobre mim",
    heroHeadline: "Explora o mundo, um waypoint de cada vez.",
    heroTagline: "Tudo para a tua próxima viagem, num só lugar: guias reais de cada país, um mapa interativo para registares onde já foste e onde queres ir, e um planeador para montares o itinerário dia a dia.",
    statsCountries: "países", statsAttractions: "atrações", statsLanguages: "línguas",
    featExploreTitle: "Explorar", featExploreDesc: "Itinerários, custos e comida reais para cada país.",
    featTrackTitle: "Registar", featTrackDesc: "Marca onde já foste e onde queres ir num mapa interativo.",
    featPlanTitle: "Planear", featPlanDesc: "Monta a tua próxima viagem dia a dia, depois exporta-a.",
    allContinents: "Todos os continentes", countries: "países", capital: "Capital",
    topAttractions: "Principais atrações", suggestedItinerary: "Itinerário sugerido", days: "dias", day: "dia",
    tripEssentials: "Essenciais da viagem", dailyBudget: "Orçamento diário", visa: "Visto",
    plugVoltage: "Tomada e voltagem", tipping: "Gorjetas", safety: "Segurança", gettingAround: "Como circular",
    gettingThere: "Como chegar", cost: "Custo", eat: "Onde comer", faqTitle: "Perguntas frequentes",
    population: "População", language: "Língua", currency: "Moeda", bestTime: "Melhor época para visitar",
    tastesOf: "Sabores de", pairsWith: "Combina bem com", bookAhead: "Reservar com antecedência",
    searchHome: "Procurar um país...", searchContinent: "Procurar países neste continente...",
    noResultsFor: "Nenhum país encontrado para", inContinent: "em",
    whereToGoNow: "Onde ir agora", whereToGoNowSubtitle: "Algumas ideias que valem a pena reservar este mês, atualizadas todos os meses.",
    monthlyEyebrow: "Atualizado mensalmente",
    quizTitle: "O Quiz do Passaporte deste mês", quizSubtitle: "8 perguntas. Quantos países consegues acertar?",
    quizStart: "Começar o quiz", quizQuestionLabel: "Pergunta", quizOf: "de",
    quizPromptTagline: "Que país é este?", quizPromptHighlight: "Que país é famoso por isto?",
    quizPromptFood: "De que país é este prato?", quizPromptFlag: "De que país é esta bandeira?",
    quizNext: "Pergunta seguinte", quizSeeResults: "Ver resultados",
    quizYourScore: "A tua pontuação", quizPlayAgain: "Jogar novamente",
    quizCopyResult: "Copiar o resultado", quizCopied: "Copiado!",
    quizShareText: "Fiz SCORE/8 no Passport Quiz da Waypoint este mês 🧳 Consegues fazer melhor?",
    quizRank0: "Acabaste de tirar o passaporte", quizRank1: "Viajante habitual", quizRank2: "Andarilho do mundo", quizRank3: "Mestre Waypoint",
    signIn: "Entrar", signOut: "Sair", createAccount: "Criar conta",
    continueWithGoogle: "Continuar com Google", orDivider: "ou",
    emailLabel: "Email", passwordLabel: "Palavra-passe",
    authSubmitSignIn: "Entrar", authSubmitSignUp: "Criar conta",
    authSwitchToSignUp: "Não tens conta? Cria uma", authSwitchToSignIn: "Já tens conta? Entra",
    nudgeTitle: "Bem-vindo ao Waypoint!", nudgeSubtitle: "Queres também a newsletter? As mesmas viagens, direto ao teu email.",
    nudgeSkip: "Talvez mais tarde",
    newsletterSubscribeBtn: "Subscrever", newsletterBusy: "A subscrever…",
    newsletterSuccess: "Feito! Fica atento à caixa de entrada para a próxima edição.",
    newsletterError: "Algo correu mal — confirma o email e tenta de novo.",
    authModalTitleIn: "Bem-vindo de volta", authModalTitleUp: "Cria a tua conta",
    authModalSubtitle: "Acompanha os países que já visitaste e os que queres conhecer a seguir.",
    markVisited: "Visitado", markWantToVisit: "Quero visitar",
    signInToTrackHint: "Entra para acompanhar este país",
    myMap: "Mapa", mapTitle: "O teu mapa", mapSubtitle: "Todos os países que marcaste, num só sítio.",
    mapLegendVisited: "Visitado", mapLegendWant: "Quero visitar", mapLegendNone: "Não marcado",
    mapSignInPrompt: "Entra para começares a marcar países no teu mapa.",
    mapVisitedListTitle: "Visitados", mapWantListTitle: "Quero visitar", mapListEmpty: "Ainda nada aqui.",
    mapLoading: "A carregar o mapa…", mapLoadError: "Não foi possível carregar o mapa. Verifica a ligação e tenta outra vez.",
    countryDetailLoading: "A carregar detalhes do país…",
    countryDetailError: "Não foi possível carregar os detalhes deste país. Verifica a ligação e tenta outra vez.", tryAgain: "Tentar outra vez",
    essentialAnchor: "Essencial", placesAnchor: "Lugares", foodAnchor: "Sabores", routeAnchor: "Roteiro", faqAnchor: "Dúvidas",
    readMore: "Ler mais", readLess: "Ler menos", showMap: "Ver mapa", hideMap: "Ocultar mapa",
    pctOfWorldVisited: "do mundo visitado",
    myTrips: "Viagens", tripsSubtitle: "Planeia a tua próxima viagem, dia a dia.",
    tripsStatTrips: "VIAGENS", tripsStatContinents: "CONTINENTES", tripsStatNights: "NOITES PLANEADAS", tripsStatDone: "CONCLUÍDAS",
    routeTab: "Percurso", daysTab: "Dias", bookingsTab: "Reservas", comingSoonBadge: "em breve",
    whereToSleepBtn: "Onde dormir", whereToEatBtn: "Onde comer",
    placesBtn: "Locais", placesCountSuffix: "locais", transportTitle: "Transporte",
    transportModeLabel: "Meio de transporte", transportDurationLabel: "Duração", transportCostLabel: "Custo",
    mapIllustrativeLabel: "Mapa ilustrativo", mapIllustrativeNote: "Percurso terrestre, não está à escala.",
    transitAddBtn: "Adicionar tempo de viagem", transitEditBtn: "Editar",
    highlightsChipLabel: "destaques", doneEditingLabel: "concluído",
    dayListEmpty: "Ainda nada planeado para este dia.", dayMapEmpty: "Adiciona um sítio a este dia para o veres no mapa.",
    openMenu: "Abrir menu", closeMenu: "Fechar menu", menuLabel: "MENU", languageLabel: "Idioma",
    signedInAs: "Sessão iniciada como", notSignedIn: "Sem sessão iniciada — toca para entrar",
    daySuggestionsLabel: "Dos teus destaques — toca para adicionar a este dia", suggestionsIn: "Sugestões em",
    pdfCoverTagline: "Uma forma tranquila e sem publicidade de explorar o mundo.",
    pdfEssentialsTitle: "Essencial de viagem", pdfAboutTitle: "Sobre",
    pdfRouteTitle: "O teu percurso", pdfFarewellTitle: "Boa viagem!",
    pdfFarewellLine: "Onde quer que estes dias te levem, esperamos que sejam tranquilos, bem regados a boa comida, e cheios de luz bonita.",
    pdfFarewellSign: "— Waypoint", pdfPopulation: "População", pdfLanguage: "Língua", pdfCurrency: "Moeda", pdfBestTime: "Melhor altura para visitar",
    addActivityPlaceholder: "nome do sítio ou atividade", activityTimePlaceholder: "hora",
    listViewLabel: "Lista", mapViewLabel: "Mapa",
    bookingsAll: "Tudo", bookingsFlights: "Voos", bookingsHotels: "Hotéis",
    flightNumberPlaceholder: "número do voo", flightTimePlaceholder: "hora", flightRefPlaceholder: "referência da reserva",
    noFlightsYet: "Ainda sem voos adicionados — muda o meio de transporte de uma paragem para \"Voo\" no Percurso para o adicionar aqui.",
    noHotelsYet: "Ainda sem dormidas adicionadas — adiciona uma em \"Onde dormir\" no Percurso.",
    confirmedLabel: "Confirmado", pendingLabel: "Por confirmar",
    documentsTitle: "Documentos", addDocumentPlaceholder: "ex: Passaporte — nº ABC123, válido até 2029",
    noDocumentsYet: "Ainda sem documentos adicionados.", viewInRoute: "Ver no Percurso",
    tripsSignInPrompt: "Entra para começares a planear uma viagem.", noTripsYet: "Ainda sem viagens — começa a planear a próxima.",
    newTrip: "Nova viagem", tripNameLabel: "nome", tripNamePlaceholder: "ex: Tailândia 2027",
    tripCountryLabel: "país", tripDatesLabel: "datas", daysWillBeCreated: "dias serão criados automaticamente",
    createTrip: "Criar viagem", tripStatusPlanning: "a planear", tripStatusDone: "feita",
    days: "dias", stops: "paragens", estimatedCost: "custo estimado", perDay: "por dia",
    cityPlaceholder: "cidade ou região", day: "dia", addHighlightPlaceholder: "adicionar highlight",
    addStop: "Adicionar paragem", chooseTransit: "escolher ligação", transitFlight: "avião", transitTrain: "comboio",
    transitBus: "autocarro", transitCar: "carro", transitBoat: "barco", transitDuration: "duração, ex: 12h",
    transitPrice: "preço, ex: €25", markTripDone: "Marcar viagem como feita", deleteTrip: "Eliminar viagem",
    confirmDeleteTrip: "Eliminar esta viagem? Não é possível desfazer.",
    whereToSleep: "Onde dormir", whereToEat: "Onde comer", nights: "noites",
    stayNamePlaceholder: "nome do hotel ou lugar", nightsPlaceholder: "noites", addMealPlaceholder: "restaurante ou prato",
    exportPdf: "Exportar PDF", typicalRange: "intervalo típico",
    insertStopHere: "inserir paragem aqui", hoursLabel: "horas", minutesLabel: "min",
    saveTrip: "Guardar", tripSaved: "Guardado",
    dayNotes: "Notas do dia", dayNotesPlaceholder: "Como correu o dia? Alguma coisa para recordar...",
    dayNotesSubtitle: "Um diário da viagem, uma nota por dia.", addNoteForDay: "+ Adicionar nota a este dia",
    shareTrip: "Partilhar viagem",
    shareTripOnDesc: "Quem tiver o link pode ver esta viagem (só leitura).",
    shareTripOffDesc: "Torna esta viagem pública para partilhares um link só de leitura.",
    copyLink: "Copiar link", linkCopied: "Link copiado",
    sharedTripBanner: "Estás a ver uma viagem partilhada — só leitura",
    sharedTripNotFound: "Esta viagem não está disponível. O link pode estar errado, ou a partilha foi desligada.",
    sharedTripLoading: "A carregar viagem…",
    planYourOwnTrip: "Planeia a tua própria viagem no Waypoint", backToWaypoint: "Voltar ao Waypoint",
    articlesComingSoon: "Guias mais longos, itinerários e notas de viagem estão a caminho — volta em breve.",
    productsComingSoon: "Guias para descarregar, listas de bagagem e ferramentas de planeamento estão a caminho — volta em breve.",
    newsletterIntro: "Recebe um novo destino no teu email todas as semanas — ideias de itinerários reais e notas de viagem, sem spam.",
    footerTagline: "Uma forma tranquila e sem anúncios de explorar o mundo, país a país.",
    footerExplore: "Explorar", footerConnect: "Contacto", footerProjectBy: "Um projeto da",
    footerBuiltFor: "Feito para quem planeia as viagens com um cuidado quase exagerado.",
  },
};

const WHERE_TO_GO_NOW = {
  1: [
    { id: "thailand", reason: { en: "Peak cool, dry season — comfortable temperatures for temples, islands, and everything in between.", pt: "Época seca e fresca no seu melhor — temperaturas agradáveis para templos, ilhas, e tudo pelo meio." } },
    { id: "costa-rica", reason: { en: "Dry season is in full swing, meaning easier wildlife spotting and calmer seas on the Pacific coast.", pt: "Época seca em pleno — mais fácil avistar vida selvagem e mar mais calmo na costa do Pacífico." } },
    { id: "new-zealand", reason: { en: "The height of southern summer — long days for hiking, beaches, and Milford Sound at its best.", pt: "O auge do verão austral — dias longos para caminhadas, praias, e Milford Sound no seu melhor." } },
  ],
  2: [
    { id: "uae", reason: { en: "One of the most pleasant stretches of the year in Dubai and Abu Dhabi, well before summer's extreme heat.", pt: "Um dos períodos mais agradáveis do ano no Dubai e Abu Dhabi, bem antes do calor extremo do verão." } },
    { id: "argentina", reason: { en: "Peak Patagonian summer — the best window for hiking around El Calafate and the glaciers.", pt: "Verão patagónico no seu auge — a melhor janela para caminhadas perto de El Calafate e os glaciares." } },
    { id: "vietnam", reason: { en: "The south's dry season is in full swing, with the north still comfortably cool and clear.", pt: "A época seca do sul está em pleno, com o norte ainda agradavelmente fresco e límpido." } },
  ],
  3: [
    { id: "japan", reason: { en: "Cherry blossoms begin their sweep north through the country from late March.", pt: "As flores de cerejeira começam a sua marcha para norte pelo país a partir de finais de março." } },
    { id: "namibia", reason: { en: "Dry season is well underway, with clear skies ideal for self-driving and stargazing.", pt: "A época seca já vai avançada, com céus limpos ideais para conduzir e observar estrelas." } },
    { id: "egypt", reason: { en: "Comfortably mild for the pyramids and Nile cruising, before summer's serious heat arrives.", pt: "Temperaturas amenas para as pirâmides e cruzeiros no Nilo, antes do calor sério do verão chegar." } },
  ],
  4: [
    { id: "netherlands", reason: { en: "Tulip season is in full color, with Keukenhof's gardens at their peak.", pt: "A época das tulipas está em pleno esplendor, com os jardins de Keukenhof no seu auge." } },
    { id: "india", reason: { en: "A pleasant window before the monsoon, with the Taj Mahal and Rajasthan at comfortable temperatures.", pt: "Uma janela agradável antes da monção, com o Taj Mahal e o Rajastão em temperaturas confortáveis." } },
    { id: "portugal", reason: { en: "Mild spring weather and thinner crowds, before the summer rush along the coast.", pt: "Clima ameno de primavera e menos multidões, antes da correria do verão na costa." } },
  ],
  5: [
    { id: "peru", reason: { en: "The dry season begins, and Machu Picchu enters its best stretch of clear, rain-free months.", pt: "Começa a época seca, e Machu Picchu entra no seu melhor período de meses límpidos e sem chuva." } },
    { id: "greece", reason: { en: "Warm enough for the islands, without the peak-summer heat or crowds of July and August.", pt: "Já quente o suficiente para as ilhas, sem o calor ou multidões do pico de julho e agosto." } },
    { id: "croatia", reason: { en: "Early-summer warmth along the Adriatic, with far fewer crowds than the July peak.", pt: "Calor de início de verão junto ao Adriático, com muito menos multidões do que o pico de julho." } },
  ],
  6: [
    { id: "iceland", reason: { en: "Midnight sun and the best weather window of the year for the Ring Road.", pt: "Sol da meia-noite e a melhor janela de clima do ano para a Ring Road." } },
    { id: "kenya", reason: { en: "The dry season begins, bringing some of the year's best wildlife viewing to the Mara.", pt: "Começa a época seca, trazendo uma das melhores alturas do ano para observar vida selvagem na Mara." } },
    { id: "switzerland", reason: { en: "Alpine trails fully open up, with long days perfect for the classic train-and-hike routes.", pt: "As trilhas alpinas abrem por completo, com dias longos perfeitos para as rotas clássicas de comboio e caminhada." } },
  ],
  7: [
    { id: "norway", reason: { en: "Midnight sun continues, with the best hiking and fjord-cruising weather of the year.", pt: "O sol da meia-noite continua, com o melhor clima do ano para caminhadas e cruzeiros pelos fiordes." } },
    { id: "tanzania", reason: { en: "The Great Migration's river crossings typically peak now in the Serengeti and Mara.", pt: "As travessias de rio da Grande Migração atingem tipicamente o seu pico agora no Serengeti e na Mara." } },
    { id: "canada", reason: { en: "Mild, sunny summer weather across the Rockies, with every national park fully open.", pt: "Clima de verão ameno e ensolarado por toda a região das Rochosas, com todos os parques nacionais totalmente abertos." } },
  ],
  8: [
    { id: "georgia", reason: { en: "Peak season for hiking the Caucasus, with mountain passes fully clear of snow.", pt: "Época alta para caminhadas no Cáucaso, com os passos de montanha totalmente livres de neve." } },
    { id: "south-africa", reason: { en: "Dry winter means sparse vegetation and excellent visibility for Kruger safaris.", pt: "O inverno seco significa vegetação escassa e excelente visibilidade para safaris no Kruger." } },
    { id: "sweden", reason: { en: "Long, warm days made for boating through the Stockholm archipelago.", pt: "Dias longos e quentes, perfeitos para navegar pelo arquipélago de Estocolmo." } },
  ],
  9: [
    { id: "turkey", reason: { en: "Warm, golden shoulder-season weather with noticeably thinner summer crowds.", pt: "Clima quente e dourado de época intermédia, com muito menos multidões de verão." } },
    { id: "botswana", reason: { en: "The dry season peaks, concentrating wildlife around the Okavango's remaining water sources.", pt: "A época seca atinge o pico, concentrando a vida selvagem junto às últimas fontes de água do Okavango." } },
    { id: "czech-republic", reason: { en: "Comfortably cool for wandering Prague's Old Town, with the summer crowds thinning out.", pt: "Temperaturas amenas para passear pela Cidade Velha de Praga, com as multidões de verão a diminuir." } },
  ],
  10: [
    { id: "chile", reason: { en: "Spring arrives in Patagonia, with wildflowers and a genuine shoulder-season calm.", pt: "A primavera chega à Patagónia, com flores silvestres e uma verdadeira calma de época intermédia." } },
    { id: "japan", reason: { en: "Autumn foliage begins its own sweep across the country, following spring's cherry blossoms in reverse.", pt: "A folhagem de outono começa a sua própria marcha pelo país, seguindo ao contrário as flores de cerejeira da primavera." } },
    { id: "vietnam", reason: { en: "The north settles into its clearest, driest stretch of the year.", pt: "O norte entra no seu período mais límpido e seco do ano." } },
  ],
  11: [
    { id: "morocco", reason: { en: "One of the two ideal windows of the year — warm days, cool nights, no summer heat.", pt: "Uma das duas janelas ideais do ano — dias quentes, noites frescas, sem o calor do verão." } },
    { id: "thailand", reason: { en: "The cool, dry season returns, bringing some of the year's most comfortable travel weather.", pt: "A época seca e fresca regressa, trazendo um dos climas mais agradáveis do ano para viajar." } },
    { id: "costa-rica", reason: { en: "The dry season begins its run through April, with clearer skies across both coasts.", pt: "A época seca começa o seu percurso até abril, com céus mais limpos em ambas as costas." } },
  ],
  12: [
    { id: "tanzania", reason: { en: "Calving season begins in the southern Serengeti, drawing predators along with it.", pt: "Começa a época de nascimentos no sul do Serengeti, atraindo predadores na mesma zona." } },
    { id: "mexico", reason: { en: "Dry season warmth makes for an easy escape from northern winter, from the Yucatán to Mexico City.", pt: "O calor da época seca torna-se uma fuga fácil ao inverno do norte, do Iucatão à Cidade do México." } },
    { id: "new-zealand", reason: { en: "Southern summer kicks off, with long days made for the Great Walks and beach time alike.", pt: "Começa o verão austral, com dias longos perfeitos tanto para as Great Walks como para a praia." } },
  ],
};

const MONTHLY_QUIZ = {
  1: ["japan", "brazil", "egypt", "france", "thailand", "kenya", "mexico", "iceland"],
  2: ["italy", "india", "morocco", "usa", "vietnam", "peru", "greece", "south-africa"],
  3: ["spain", "china", "argentina", "uk", "cambodia", "tanzania", "portugal", "uae"],
  4: ["germany", "indonesia", "colombia", "canada", "laos", "botswana", "netherlands", "oman"],
  5: ["turkey", "malaysia", "chile", "australia", "singapore", "namibia", "ireland", "qatar"],
  6: ["austria", "croatia", "ecuador", "new-zealand", "cabo-verde", "zambia", "switzerland", "panama"],
  7: ["norway", "poland", "bolivia", "costa-rica", "mauritius", "zimbabwe", "denmark", "belize"],
  8: ["sweden", "czech-republic", "bosnia", "fiji", "kuwait", "georgia", "belgium", "vanuatu"],
  9: ["turkey", "china", "mexico", "greece", "laos", "botswana", "spain", "oman"],
  10: ["japan", "italy", "brazil", "morocco", "thailand", "kenya", "france", "peru"],
  11: ["india", "egypt", "vietnam", "usa", "argentina", "south-africa", "uk", "cambodia"],
  12: ["germany", "netherlands", "canada", "colombia", "indonesia", "tanzania", "uae", "iceland"],
};

const ABOUT_BIO = {
  en: [
    "Hi, I'm José Maria Garcia — the person behind Waypoint.",
    "For as long as I can remember, I've been chasing the same question: how do we live more consciously, more aligned with who we actually are? That question has taken me through some very different worlds — engineering, theatre, leadership, and a fair amount of quiet self-exploration.",
    "It started at Instituto Superior Técnico in Lisbon, where engineering taught me to think in structures and take apart hard problems piece by piece. But something was missing, so I followed my curiosity into theatre and film, including a stretch in Los Angeles that was pure discovery — expression without a blueprint. Eventually I came back to tech, working my way into engineering leadership across a few telecom and technology companies. Along the way, yoga, meditation, and a lot of quiet reflection became less of a side interest and more of a daily practice — the thing that actually kept me clear-headed and present through all the pivots.",
    "Travel, it turns out, was never really separate from any of this. It's just another way of asking the same question in a different place.",
    "I've loved traveling for as long as I can remember. When I was six, I made my father a deal: he'd pay for a trip to the jungles of Borneo. He never did pay up — but I went anyway, years later, and I still bring it up every chance I get.",
    "Since then, a few places have stuck with me more than most. Thailand, for its warmth and color, and a kind of everyday hospitality that's hard to describe until you've experienced it. Iceland, for landscapes so raw and vast they make you feel appropriately small. Namibia, for the sheer scale of its silence — deserts and skies that put everything else in perspective.",
    "My mission with Waypoint is simple: to organize travel information in a way that's actually easy to use, for anyone planning a trip — no clutter, no guesswork, just what you need to go somewhere and get it right. The same clarity I've spent years chasing in everything else, I want this site to hand to you before you even land.",
  ],
  pt: [
    "Olá, sou o José Maria Garcia — a pessoa por trás do Waypoint.",
    "Ao longo da minha vida persegui sempre a mesma pergunta: como podemos viver de forma mais consciente, mais alinhados com aquilo que realmente somos? Essa pergunta levou-me por mundos muito diferentes — engenharia, teatro, liderança, e uma boa dose de exploração pessoal silenciosa.",
    "Começou no Instituto Superior Técnico, em Lisboa, onde a engenharia me ensinou a pensar de forma estruturada e a desmontar problemas complexos peça por peça. Mas faltava algo, e essa curiosidade levou-me ao teatro e ao cinema, incluindo uma passagem por Los Angeles que foi pura descoberta — expressão sem plano definido. Mais tarde regressei ao mundo tecnológico, evoluindo até posições de liderança em engenharia em várias empresas de telecomunicações e tecnologia. Pelo caminho, o yoga, a meditação e muita reflexão silenciosa deixaram de ser um interesse paralelo para se tornarem uma prática diária — aquilo que realmente me manteve claro e presente ao longo de todas as viragens.",
    "As viagens, afinal, nunca estiveram realmente separadas de tudo isto. São só outra forma de fazer a mesma pergunta num lugar diferente.",
    "Sempre gostei de viajar, desde que me lembro. Quando tinha seis anos, fiz um acordo com o meu pai: ele pagaria uma viagem à selva de Bornéu. Nunca chegou a pagar — mas fui na mesma, anos depois, e ainda hoje faço questão de o lembrar disso sempre que posso.",
    "Desde então, alguns lugares ficaram comigo mais do que outros. A Tailândia, pelo seu calor humano e cor, e uma hospitalidade do dia a dia difícil de descrever sem a viver. A Islândia, por paisagens tão cruas e vastas que nos fazem sentir devidamente pequenos. A Namíbia, pela escala pura do seu silêncio — desertos e céus que colocam tudo o resto em perspetiva.",
    "A minha missão com o Waypoint é simples: organizar a informação de viagem de uma forma verdadeiramente fácil de usar, para qualquer pessoa a planear uma viagem — sem ruído, sem tentativa e erro, só o que precisas para ires a um lugar e acertares. A mesma clareza que persegui durante anos em tudo o resto, quero que este site te entregue antes mesmo de aterrares.",
  ],
};

function localizeCountry(c, lang) {
  const p = lang === "pt" ? c.pt : null;
  const base = {
    ...c,
    name: (p && p.name) || c.name,
    capital: (p && p.capital) || c.capital,
    population: (p && p.population) || c.population,
    language: (p && p.language) || c.language,
    currency: (p && p.currency) || c.currency,
    bestTime: (p && p.bestTime) || c.bestTime,
    tagline: (p && p.tagline) || c.tagline,
    highlights: (p && p.highlights) || c.highlights,
    blurb: (p && p.blurb) || c.blurb,
    budget: (p && p.budget) || c.budget,
  };
  if (!p) return base;
  return {
    ...base,
    visa: p.visa || c.visa,
    goodToKnow: p.goodToKnow || c.goodToKnow,
    food: p.food || c.food,
    attractions: c.attractions ? c.attractions.map((a, i) => (p.attractions && p.attractions[i]) ? { ...a, name: p.attractions[i].name, desc: p.attractions[i].desc } : a) : c.attractions,
    itinerary: c.itinerary ? c.itinerary.map((s, i) => (p.itinerary && p.itinerary[i]) ? {
      ...s,
      label: p.itinerary[i].label || s.label,
      title: p.itinerary[i].title || s.title,
      desc: p.itinerary[i].desc || s.desc,
      logistics: p.itinerary[i].logistics !== undefined ? p.itinerary[i].logistics : s.logistics,
    } : s) : c.itinerary,
  };
}

function localizeContinent(cont, lang) {
  const p = lang === "pt" ? cont.pt : null;
  return {
    ...cont,
    name: (p && p.name) || cont.name,
    tagline: (p && p.tagline) || cont.tagline,
    countries: cont.countries.map((c) => localizeCountry(c, lang)),
  };
}

/* ---------- decorative homepage hero: globe + plane ---------- */
function HeroIllustration() {
  return (
    <svg viewBox="0 0 400 190" className="wp-hero-svg" xmlns="http://www.w3.org/2000/svg">
      <g opacity="0.9">
        <circle cx="140" cy="100" r="72" fill="none" stroke="#16233B" strokeWidth="1.6" />
        <ellipse cx="140" cy="100" rx="72" ry="24" fill="none" stroke="#16233B" strokeWidth="1" opacity="0.55" />
        <ellipse cx="140" cy="100" rx="72" ry="48" fill="none" stroke="#16233B" strokeWidth="1" opacity="0.4" />
        <ellipse cx="140" cy="100" rx="24" ry="72" fill="none" stroke="#16233B" strokeWidth="1" opacity="0.55" />
        <line x1="68" y1="100" x2="212" y2="100" stroke="#16233B" strokeWidth="1" opacity="0.4" />
        <circle cx="112" cy="72" r="2.6" fill="#B0552E" />
        <circle cx="168" cy="120" r="2.6" fill="#C9A24B" />
        <circle cx="122" cy="132" r="2.6" fill="#2F5D62" />
        <circle cx="178" cy="66" r="2.6" fill="#7A4E5C" />
      </g>
      <path d="M40 150 C 100 60, 220 40, 330 55" fill="none" stroke="#C9A24B" strokeWidth="1.4" strokeDasharray="1 7" strokeLinecap="round" />
      <g transform="translate(318,46) rotate(28)">
        <path d="M0 8 L26 2 L34 5 L27 9 L20 22 L15 21 L17 10 L8 12 L4 18 L0 16 L3 9 Z" fill="#16233B" />
      </g>
    </svg>
  );
}

/* ---------- country map with itinerary route (Leaflet + free CartoDB tiles) ---------- */
function CountryMap({ country, accentColor }) {
  const containerRef = useRef(null);
  const mapRef = useRef(null);

  const stops = (country.itinerary || []).filter((s) => typeof s.lat === "number" && typeof s.lng === "number");

  useEffect(() => {
    if (!containerRef.current || !window.L || stops.length === 0) return;

    const map = window.L.map(containerRef.current, { zoomControl: true, scrollWheelZoom: false });
    mapRef.current = map;

    window.L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; OpenStreetMap contributors',
      maxZoom: 18,
    }).addTo(map);

    const latlngs = stops.map((s) => [s.lat, s.lng]);

    stops.forEach((s, i) => {
      const icon = window.L.divIcon({
        className: "wp-map-pin",
        html: '<div class="wp-map-pin-inner" style="background:' + accentColor + '">' + (i + 1) + "</div>",
        iconSize: [26, 26],
        iconAnchor: [13, 13],
      });
      window.L.marker([s.lat, s.lng], { icon }).addTo(map).bindTooltip(escapeHtml(s.title || s.label), { direction: "top", offset: [0, -12] });
    });

    if (latlngs.length > 1) {
      window.L.polyline(latlngs, { color: accentColor, weight: 2, dashArray: "5 7", opacity: 0.85 }).addTo(map);
      map.fitBounds(window.L.latLngBounds(latlngs), { padding: [28, 28] });
    } else {
      map.setView(latlngs[0], 6);
    }

    return () => { map.remove(); };
  }, [country.id]);

  if (stops.length === 0) return null;

  return <div ref={containerRef} className="wp-map" />;
}

/* ---------- Trip planner map: geocodes user-typed city names on demand (free, keyless Nominatim/OpenStreetMap lookup) ---------- */
function TripMap({ trip, countryName, geocodeCache, geocodeCity, accentColor, T }) {
  const containerRef = useRef(null);
  const mapRef = useRef(null);

  const points = (trip.stops || []).map((s, i) => {
    const key = ((s.city || "") + "|" + (countryName || "")).toLowerCase();
    const hit = geocodeCache[key];
    return { stop: s, index: i, hit };
  });

  useEffect(() => {
    (trip.stops || []).forEach((s) => { if (s.city && s.city.trim()) geocodeCity(s.city.trim(), countryName); });
    // eslint-disable-next-line
  }, [JSON.stringify((trip.stops || []).map((s) => s.city)), countryName]);

  const resolved = points.filter((p) => p.hit && p.hit.lat);
  const stillLoading = points.some((p) => p.hit === "loading");

  useEffect(() => {
    if (!containerRef.current || !window.L || resolved.length === 0) return;
    const map = window.L.map(containerRef.current, { zoomControl: true, scrollWheelZoom: false });
    mapRef.current = map;
    window.L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; OpenStreetMap contributors',
      maxZoom: 18,
    }).addTo(map);

    const latlngs = resolved.map((p) => [p.hit.lat, p.hit.lng]);
    resolved.forEach((p) => {
      const icon = window.L.divIcon({
        className: "wp-map-pin",
        html: '<div class="wp-map-pin-inner" style="background:' + accentColor + '">' + (p.index + 1) + "</div>",
        iconSize: [26, 26],
        iconAnchor: [13, 13],
      });
      window.L.marker([p.hit.lat, p.hit.lng], { icon }).addTo(map).bindTooltip(escapeHtml(p.stop.city), { direction: "top", offset: [0, -12] });
    });
    if (latlngs.length > 1) {
      window.L.polyline(latlngs, { color: accentColor, weight: 2, dashArray: "5 7", opacity: 0.85 }).addTo(map);
      map.fitBounds(window.L.latLngBounds(latlngs), { padding: [28, 28] });
    } else {
      map.setView(latlngs[0], 6);
    }
    return () => { map.remove(); };
  }, [resolved.map((p) => p.stop.city + p.hit.lat).join(",")]);

  return (
    <div className="wp-trip-map-panel">
      <p className="wp-trip-map-label">{T.mapIllustrativeLabel}</p>
      {resolved.length > 0 ? (
        <div ref={containerRef} className="wp-trip-map" />
      ) : (
        <div className="wp-trip-map wp-trip-map-empty">
          {stillLoading ? <span className="wp-map-loading-spinner"></span> : null}
        </div>
      )}
      <p className="wp-trip-map-note">{T.mapIllustrativeNote}</p>
    </div>
  );
}

/* ---------- Day map: same geocoding mechanism, scoped to one day's activities ---------- */
function DayMap({ activities, cityName, countryName, geocodeCache, geocodeCity, accentColor, T }) {
  const containerRef = useRef(null);
  const mapRef = useRef(null);

  const locationContext = [cityName, countryName].filter(Boolean).join(", ");
  const points = activities.map((a, i) => {
    const key = ((a.name || "") + "|" + locationContext).toLowerCase();
    const hit = geocodeCache[key];
    return { activity: a, index: i, hit, key };
  });

  useEffect(() => {
    activities.forEach((a) => { if (a.name && a.name.trim()) geocodeCity(a.name.trim(), locationContext); });
    // eslint-disable-next-line
  }, [JSON.stringify(activities.map((a) => a.name)), locationContext]);

  const resolved = points.filter((p) => p.hit && p.hit.lat);
  const stillLoading = points.some((p) => p.hit === "loading");

  useEffect(() => {
    if (!containerRef.current || !window.L || resolved.length === 0) return;
    const map = window.L.map(containerRef.current, { zoomControl: true, scrollWheelZoom: false });
    mapRef.current = map;
    window.L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; OpenStreetMap contributors',
      maxZoom: 18,
    }).addTo(map);

    const latlngs = resolved.map((p) => [p.hit.lat, p.hit.lng]);
    resolved.forEach((p) => {
      const icon = window.L.divIcon({
        className: "wp-map-pin",
        html: '<div class="wp-map-pin-inner" style="background:' + accentColor + '">' + (p.index + 1) + "</div>",
        iconSize: [26, 26],
        iconAnchor: [13, 13],
      });
      window.L.marker([p.hit.lat, p.hit.lng], { icon }).addTo(map).bindTooltip(escapeHtml(p.activity.name), { direction: "top", offset: [0, -12] });
    });
    if (latlngs.length > 1) {
      window.L.polyline(latlngs, { color: accentColor, weight: 2, dashArray: "5 7", opacity: 0.85 }).addTo(map);
      map.fitBounds(window.L.latLngBounds(latlngs), { padding: [28, 28] });
    } else {
      map.setView(latlngs[0], 14);
    }
    return () => { map.remove(); };
  }, [resolved.map((p) => p.activity.name + p.hit.lat).join(",")]);

  if (activities.length === 0) {
    return (
      <div className="wp-trip-map-panel">
        <div className="wp-trip-map wp-trip-map-empty"><span className="wp-day-map-empty-text">{T.dayMapEmpty}</span></div>
      </div>
    );
  }

  return (
    <div className="wp-trip-map-panel">
      <p className="wp-trip-map-label">{T.mapIllustrativeLabel}</p>
      {resolved.length > 0 ? (
        <div ref={containerRef} className="wp-trip-map" />
      ) : (
        <div className="wp-trip-map wp-trip-map-empty">
          {stillLoading ? <span className="wp-map-loading-spinner"></span> : <span className="wp-day-map-empty-text">{T.dayMapEmpty}</span>}
        </div>
      )}
    </div>
  );
}

/* ---------- Newsletter signup, backed by Firestore (single source of truth) ---------- */
function NewsletterSignupForm({ user, T }) {
  const [email, setEmail] = useState(user ? (user.email || "") : "");
  const [status, setStatus] = useState("idle"); // idle | busy | done | error

  const submit = () => {
    const trimmed = (email || "").trim().toLowerCase();
    if (!trimmed || trimmed.indexOf("@") < 1 || !window.firebase) { setStatus("error"); return; }
    setStatus("busy");
    const docId = trimmed.replace(/[^a-z0-9@._-]/g, "_");
    const payload = {
      email: trimmed,
      subscribedAt: firebase.firestore.FieldValue.serverTimestamp(),
      uid: user ? user.uid : null,
    };
    firebase.firestore().collection("newsletter_subscribers").doc(docId).set(payload, { merge: true })
      .then(() => {
        if (user) {
          firebase.firestore().collection("users").doc(user.uid).set({ newsletterSubscribed: true }, { merge: true }).catch(() => {});
        }
        setStatus("done");
      })
      .catch(() => setStatus("error"));
  };

  if (status === "done") {
    return <p className="wp-newsletter-success">{T.newsletterSuccess}</p>;
  }

  return (
    <div className="wp-newsletter-form">
      <input
        type="email"
        className="wp-auth-input"
        placeholder={T.emailLabel}
        value={email}
        onChange={(e) => { setEmail(e.target.value); setStatus("idle"); }}
        onKeyDown={(e) => { if (e.key === "Enter") submit(); }}
      />
      {status === "error" && <p className="wp-auth-error">{T.newsletterError}</p>}
      <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ width: "100%", justifyContent: "center" }} onClick={submit} disabled={status === "busy"}>
        {status === "busy" ? T.newsletterBusy : T.newsletterSubscribeBtn}
      </button>
    </div>
  );
}

/* ---------- Wikipedia thumbnail (fetched at runtime, cached in-memory) ---------- */
const wikiImageCache = {};
function AttractionImage({ title, alt }) {
  const [state, setState] = useState(wikiImageCache[title] ? "done" : "loading");
  const [src, setSrc] = useState(wikiImageCache[title] || null);

  useEffect(() => {
    let cancelled = false;
    if (wikiImageCache[title] !== undefined) {
      setSrc(wikiImageCache[title]);
      setState(wikiImageCache[title] ? "done" : "empty");
      return;
    }
    fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + encodeURIComponent(title))
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        if (cancelled) return;
        const url = data && data.thumbnail && data.thumbnail.source ? data.thumbnail.source : null;
        wikiImageCache[title] = url;
        setSrc(url);
        setState(url ? "done" : "empty");
      })
      .catch(() => {
        if (cancelled) return;
        wikiImageCache[title] = null;
        setState("empty");
      });
    return () => { cancelled = true; };
  }, [title]);

  if (state === "loading") {
    return <div className="wp-attraction-img wp-attraction-img-loading" />;
  }
  if (state === "empty" || !src) {
    return (
      <div className="wp-attraction-img wp-attraction-img-empty">
        <ImageOff size={32} style={{ color: "#c9bfa6" }} />
      </div>
    );
  }
  return <img className="wp-attraction-img" src={src} alt={alt} loading="lazy" />;
}

function StatBlock({ icon: Icon, label, value, accent }) {
  return (
    <div style={{ display: "flex", gap: "0.65rem", alignItems: "flex-start" }}>
      <Icon size={17} style={{ color: accent, marginTop: "2px", flexShrink: 0 }} />
      <div>
        <div style={{ fontSize: "0.95rem", color: "#262119", fontWeight: 500, lineHeight: 1.3 }}>{value}</div>
        <div style={{ fontSize: "0.78rem", color: "#8a8272", marginTop: "1px" }}>{label}</div>
      </div>
    </div>
  );
}

function StatusDot({ status }) {
  if (!status) return null;
  return <span className={"wp-status-dot wp-status-dot-" + status} title={status} />;
}

const WORLD_MAP_META = {"ad":{"nameEn":"Andorra","namePt":"Andorra","contEn":"Europe","contPt":"Europa"},"ae":{"nameEn":"United Arab Emirates","namePt":"Emirados Árabes Unidos","contEn":"Asia","contPt":"Ásia"},"af":{"nameEn":"Afghanistan","namePt":"Afeganistão","contEn":"Asia","contPt":"Ásia"},"ag":{"nameEn":"Antigua and Barbuda","namePt":"Antígua e Barbuda","contEn":"North America","contPt":"América do Norte"},"al":{"nameEn":"Albania","namePt":"Albânia","contEn":"Europe","contPt":"Europa"},"am":{"nameEn":"Armenia","namePt":"Arménia","contEn":"Asia","contPt":"Ásia"},"ao":{"nameEn":"Angola","namePt":"Angola","contEn":"Africa","contPt":"África"},"ar":{"nameEn":"Argentina","namePt":"Argentina","contEn":"South America","contPt":"América do Sul"},"at":{"nameEn":"Austria","namePt":"Áustria","contEn":"Europe","contPt":"Europa"},"au":{"nameEn":"Australia","namePt":"Austrália","contEn":"Oceania","contPt":"Oceânia"},"az":{"nameEn":"Azerbaijan","namePt":"Azerbaijão","contEn":"Asia","contPt":"Ásia"},"ba":{"nameEn":"Bosnia and Herzegovina","namePt":"Bósnia e Herzegovina","contEn":"Europe","contPt":"Europa"},"bb":{"nameEn":"Barbados","namePt":"Barbados","contEn":"North America","contPt":"América do Norte"},"bd":{"nameEn":"Bangladesh","namePt":"Bangladesh","contEn":"Asia","contPt":"Ásia"},"be":{"nameEn":"Belgium","namePt":"Bélgica","contEn":"Europe","contPt":"Europa"},"bf":{"nameEn":"Burkina Faso","namePt":"Burquina Faso","contEn":"Africa","contPt":"África"},"bg":{"nameEn":"Bulgaria","namePt":"Bulgária","contEn":"Europe","contPt":"Europa"},"bh":{"nameEn":"Bahrain","namePt":"Barém","contEn":"Asia","contPt":"Ásia"},"bi":{"nameEn":"Burundi","namePt":"Burundi","contEn":"Africa","contPt":"África"},"bj":{"nameEn":"Benin","namePt":"Benim","contEn":"Africa","contPt":"África"},"bn":{"nameEn":"Brunei","namePt":"Brunei","contEn":"Asia","contPt":"Ásia"},"bo":{"nameEn":"Bolivia","namePt":"Bolívia","contEn":"South America","contPt":"América do Sul"},"br":{"nameEn":"Brazil","namePt":"Brasil","contEn":"South America","contPt":"América do Sul"},"bs":{"nameEn":"Bahamas","namePt":"Baamas","contEn":"North America","contPt":"América do Norte"},"bt":{"nameEn":"Bhutan","namePt":"Butão","contEn":"Asia","contPt":"Ásia"},"bw":{"nameEn":"Botswana","namePt":"Botsuana","contEn":"Africa","contPt":"África"},"by":{"nameEn":"Belarus","namePt":"Bielorrússia","contEn":"Europe","contPt":"Europa"},"bz":{"nameEn":"Belize","namePt":"Belize","contEn":"North America","contPt":"América do Norte"},"ca":{"nameEn":"Canada","namePt":"Canadá","contEn":"North America","contPt":"América do Norte"},"cd":{"nameEn":"DR Congo","namePt":"RD Congo","contEn":"Africa","contPt":"África"},"cf":{"nameEn":"Central African Republic","namePt":"República Centro-Africana","contEn":"Africa","contPt":"África"},"cg":{"nameEn":"Republic of the Congo","namePt":"República do Congo","contEn":"Africa","contPt":"África"},"ch":{"nameEn":"Switzerland","namePt":"Suíça","contEn":"Europe","contPt":"Europa"},"ci":{"nameEn":"Côte d'Ivoire","namePt":"Costa do Marfim","contEn":"Africa","contPt":"África"},"cl":{"nameEn":"Chile","namePt":"Chile","contEn":"South America","contPt":"América do Sul"},"cm":{"nameEn":"Cameroon","namePt":"Camarões","contEn":"Africa","contPt":"África"},"cn":{"nameEn":"China","namePt":"China","contEn":"Asia","contPt":"Ásia"},"co":{"nameEn":"Colombia","namePt":"Colômbia","contEn":"South America","contPt":"América do Sul"},"cr":{"nameEn":"Costa Rica","namePt":"Costa Rica","contEn":"North America","contPt":"América do Norte"},"cu":{"nameEn":"Cuba","namePt":"Cuba","contEn":"North America","contPt":"América do Norte"},"cv":{"nameEn":"Cabo Verde","namePt":"Cabo Verde","contEn":"Africa","contPt":"África"},"cy":{"nameEn":"Cyprus","namePt":"Chipre","contEn":"Europe","contPt":"Europa"},"cz":{"nameEn":"Czech Republic","namePt":"Chéquia","contEn":"Europe","contPt":"Europa"},"de":{"nameEn":"Germany","namePt":"Alemanha","contEn":"Europe","contPt":"Europa"},"dj":{"nameEn":"Djibouti","namePt":"Jibuti","contEn":"Africa","contPt":"África"},"dk":{"nameEn":"Denmark","namePt":"Dinamarca","contEn":"Europe","contPt":"Europa"},"dm":{"nameEn":"Dominica","namePt":"Dominica","contEn":"North America","contPt":"América do Norte"},"do":{"nameEn":"Dominican Republic","namePt":"República Dominicana","contEn":"North America","contPt":"América do Norte"},"dz":{"nameEn":"Algeria","namePt":"Argélia","contEn":"Africa","contPt":"África"},"ec":{"nameEn":"Ecuador","namePt":"Equador","contEn":"South America","contPt":"América do Sul"},"ee":{"nameEn":"Estonia","namePt":"Estónia","contEn":"Europe","contPt":"Europa"},"eg":{"nameEn":"Egypt","namePt":"Egito","contEn":"Africa","contPt":"África"},"er":{"nameEn":"Eritrea","namePt":"Eritreia","contEn":"Africa","contPt":"África"},"es":{"nameEn":"Spain","namePt":"Espanha","contEn":"Europe","contPt":"Europa"},"et":{"nameEn":"Ethiopia","namePt":"Etiópia","contEn":"Africa","contPt":"África"},"fi":{"nameEn":"Finland","namePt":"Finlândia","contEn":"Europe","contPt":"Europa"},"fj":{"nameEn":"Fiji","namePt":"Fiji","contEn":"Oceania","contPt":"Oceânia"},"fm":{"nameEn":"Micronesia","namePt":"Micronésia","contEn":"Oceania","contPt":"Oceânia"},"fr":{"nameEn":"France","namePt":"França","contEn":"Europe","contPt":"Europa"},"ga":{"nameEn":"Gabon","namePt":"Gabão","contEn":"Africa","contPt":"África"},"gb":{"nameEn":"United Kingdom","namePt":"Reino Unido","contEn":"Europe","contPt":"Europa"},"gd":{"nameEn":"Grenada","namePt":"Granada","contEn":"North America","contPt":"América do Norte"},"ge":{"nameEn":"Georgia","namePt":"Geórgia","contEn":"Asia","contPt":"Ásia"},"gh":{"nameEn":"Ghana","namePt":"Gana","contEn":"Africa","contPt":"África"},"gm":{"nameEn":"Gambia","namePt":"Gâmbia","contEn":"Africa","contPt":"África"},"gn":{"nameEn":"Guinea","namePt":"Guiné","contEn":"Africa","contPt":"África"},"gq":{"nameEn":"Equatorial Guinea","namePt":"Guiné Equatorial","contEn":"Africa","contPt":"África"},"gr":{"nameEn":"Greece","namePt":"Grécia","contEn":"Europe","contPt":"Europa"},"gt":{"nameEn":"Guatemala","namePt":"Guatemala","contEn":"North America","contPt":"América do Norte"},"gw":{"nameEn":"Guinea-Bissau","namePt":"Guiné-Bissau","contEn":"Africa","contPt":"África"},"gy":{"nameEn":"Guyana","namePt":"Guiana","contEn":"South America","contPt":"América do Sul"},"hn":{"nameEn":"Honduras","namePt":"Honduras","contEn":"North America","contPt":"América do Norte"},"hr":{"nameEn":"Croatia","namePt":"Croácia","contEn":"Europe","contPt":"Europa"},"ht":{"nameEn":"Haiti","namePt":"Haiti","contEn":"North America","contPt":"América do Norte"},"hu":{"nameEn":"Hungary","namePt":"Hungria","contEn":"Europe","contPt":"Europa"},"id":{"nameEn":"Indonesia","namePt":"Indonésia","contEn":"Asia","contPt":"Ásia"},"ie":{"nameEn":"Ireland","namePt":"Irlanda","contEn":"Europe","contPt":"Europa"},"il":{"nameEn":"Israel","namePt":"Israel","contEn":"Asia","contPt":"Ásia"},"in":{"nameEn":"India","namePt":"Índia","contEn":"Asia","contPt":"Ásia"},"iq":{"nameEn":"Iraq","namePt":"Iraque","contEn":"Asia","contPt":"Ásia"},"ir":{"nameEn":"Iran","namePt":"Irão","contEn":"Asia","contPt":"Ásia"},"is":{"nameEn":"Iceland","namePt":"Islândia","contEn":"Europe","contPt":"Europa"},"it":{"nameEn":"Italy","namePt":"Itália","contEn":"Europe","contPt":"Europa"},"jm":{"nameEn":"Jamaica","namePt":"Jamaica","contEn":"North America","contPt":"América do Norte"},"jo":{"nameEn":"Jordan","namePt":"Jordânia","contEn":"Asia","contPt":"Ásia"},"jp":{"nameEn":"Japan","namePt":"Japão","contEn":"Asia","contPt":"Ásia"},"ke":{"nameEn":"Kenya","namePt":"Quénia","contEn":"Africa","contPt":"África"},"kg":{"nameEn":"Kyrgyzstan","namePt":"Quirguistão","contEn":"Asia","contPt":"Ásia"},"kh":{"nameEn":"Cambodia","namePt":"Camboja","contEn":"Asia","contPt":"Ásia"},"ki":{"nameEn":"Kiribati","namePt":"Quiribati","contEn":"Oceania","contPt":"Oceânia"},"km":{"nameEn":"Comoros","namePt":"Comores","contEn":"Africa","contPt":"África"},"kn":{"nameEn":"St Kitts and Nevis","namePt":"São Cristóvão e Neves","contEn":"North America","contPt":"América do Norte"},"kp":{"nameEn":"North Korea","namePt":"Coreia do Norte","contEn":"Asia","contPt":"Ásia"},"kr":{"nameEn":"South Korea","namePt":"Coreia do Sul","contEn":"Asia","contPt":"Ásia"},"kw":{"nameEn":"Kuwait","namePt":"Kuwait","contEn":"Asia","contPt":"Ásia"},"kz":{"nameEn":"Kazakhstan","namePt":"Cazaquistão","contEn":"Asia","contPt":"Ásia"},"la":{"nameEn":"Laos","namePt":"Laos","contEn":"Asia","contPt":"Ásia"},"lb":{"nameEn":"Lebanon","namePt":"Líbano","contEn":"Asia","contPt":"Ásia"},"lc":{"nameEn":"St Lucia","namePt":"Santa Lúcia","contEn":"North America","contPt":"América do Norte"},"li":{"nameEn":"Liechtenstein","namePt":"Listenstaine","contEn":"Europe","contPt":"Europa"},"lk":{"nameEn":"Sri Lanka","namePt":"Sri Lanka","contEn":"Asia","contPt":"Ásia"},"lr":{"nameEn":"Liberia","namePt":"Libéria","contEn":"Africa","contPt":"África"},"ls":{"nameEn":"Lesotho","namePt":"Lesoto","contEn":"Africa","contPt":"África"},"lt":{"nameEn":"Lithuania","namePt":"Lituânia","contEn":"Europe","contPt":"Europa"},"lu":{"nameEn":"Luxembourg","namePt":"Luxemburgo","contEn":"Europe","contPt":"Europa"},"lv":{"nameEn":"Latvia","namePt":"Letónia","contEn":"Europe","contPt":"Europa"},"ly":{"nameEn":"Libya","namePt":"Líbia","contEn":"Africa","contPt":"África"},"ma":{"nameEn":"Morocco","namePt":"Marrocos","contEn":"Africa","contPt":"África"},"mc":{"nameEn":"Monaco","namePt":"Mónaco","contEn":"Europe","contPt":"Europa"},"md":{"nameEn":"Moldova","namePt":"Moldávia","contEn":"Europe","contPt":"Europa"},"me":{"nameEn":"Montenegro","namePt":"Montenegro","contEn":"Europe","contPt":"Europa"},"mg":{"nameEn":"Madagascar","namePt":"Madagáscar","contEn":"Africa","contPt":"África"},"mh":{"nameEn":"Marshall Islands","namePt":"Ilhas Marshall","contEn":"Oceania","contPt":"Oceânia"},"mk":{"nameEn":"North Macedonia","namePt":"Macedónia do Norte","contEn":"Europe","contPt":"Europa"},"ml":{"nameEn":"Mali","namePt":"Mali","contEn":"Africa","contPt":"África"},"mm":{"nameEn":"Myanmar","namePt":"Myanmar","contEn":"Asia","contPt":"Ásia"},"mn":{"nameEn":"Mongolia","namePt":"Mongólia","contEn":"Asia","contPt":"Ásia"},"mr":{"nameEn":"Mauritania","namePt":"Mauritânia","contEn":"Africa","contPt":"África"},"mt":{"nameEn":"Malta","namePt":"Malta","contEn":"Europe","contPt":"Europa"},"mu":{"nameEn":"Mauritius","namePt":"Maurícia","contEn":"Africa","contPt":"África"},"mv":{"nameEn":"Maldives","namePt":"Maldivas","contEn":"Asia","contPt":"Ásia"},"mw":{"nameEn":"Malawi","namePt":"Maláui","contEn":"Africa","contPt":"África"},"mx":{"nameEn":"Mexico","namePt":"México","contEn":"North America","contPt":"América do Norte"},"my":{"nameEn":"Malaysia","namePt":"Malásia","contEn":"Asia","contPt":"Ásia"},"mz":{"nameEn":"Mozambique","namePt":"Moçambique","contEn":"Africa","contPt":"África"},"na":{"nameEn":"Namibia","namePt":"Namíbia","contEn":"Africa","contPt":"África"},"ne":{"nameEn":"Niger","namePt":"Níger","contEn":"Africa","contPt":"África"},"ng":{"nameEn":"Nigeria","namePt":"Nigéria","contEn":"Africa","contPt":"África"},"ni":{"nameEn":"Nicaragua","namePt":"Nicarágua","contEn":"North America","contPt":"América do Norte"},"nl":{"nameEn":"Netherlands","namePt":"Países Baixos","contEn":"Europe","contPt":"Europa"},"no":{"nameEn":"Norway","namePt":"Noruega","contEn":"Europe","contPt":"Europa"},"np":{"nameEn":"Nepal","namePt":"Nepal","contEn":"Asia","contPt":"Ásia"},"nr":{"nameEn":"Nauru","namePt":"Nauru","contEn":"Oceania","contPt":"Oceânia"},"nz":{"nameEn":"New Zealand","namePt":"Nova Zelândia","contEn":"Oceania","contPt":"Oceânia"},"om":{"nameEn":"Oman","namePt":"Omã","contEn":"Asia","contPt":"Ásia"},"pa":{"nameEn":"Panama","namePt":"Panamá","contEn":"North America","contPt":"América do Norte"},"pe":{"nameEn":"Peru","namePt":"Peru","contEn":"South America","contPt":"América do Sul"},"pg":{"nameEn":"Papua New Guinea","namePt":"Papua-Nova Guiné","contEn":"Oceania","contPt":"Oceânia"},"ph":{"nameEn":"Philippines","namePt":"Filipinas","contEn":"Asia","contPt":"Ásia"},"pk":{"nameEn":"Pakistan","namePt":"Paquistão","contEn":"Asia","contPt":"Ásia"},"pl":{"nameEn":"Poland","namePt":"Polónia","contEn":"Europe","contPt":"Europa"},"ps":{"nameEn":"Palestine","namePt":"Palestina","contEn":"Asia","contPt":"Ásia"},"pt":{"nameEn":"Portugal","namePt":"Portugal","contEn":"Europe","contPt":"Europa"},"pw":{"nameEn":"Palau","namePt":"Palau","contEn":"Oceania","contPt":"Oceânia"},"py":{"nameEn":"Paraguay","namePt":"Paraguai","contEn":"South America","contPt":"América do Sul"},"qa":{"nameEn":"Qatar","namePt":"Catar","contEn":"Asia","contPt":"Ásia"},"ro":{"nameEn":"Romania","namePt":"Roménia","contEn":"Europe","contPt":"Europa"},"rs":{"nameEn":"Serbia","namePt":"Sérvia","contEn":"Europe","contPt":"Europa"},"ru":{"nameEn":"Russia","namePt":"Rússia","contEn":"Europe","contPt":"Europa"},"rw":{"nameEn":"Rwanda","namePt":"Ruanda","contEn":"Africa","contPt":"África"},"sa":{"nameEn":"Saudi Arabia","namePt":"Arábia Saudita","contEn":"Asia","contPt":"Ásia"},"sb":{"nameEn":"Solomon Islands","namePt":"Ilhas Salomão","contEn":"Oceania","contPt":"Oceânia"},"sc":{"nameEn":"Seychelles","namePt":"Seicheles","contEn":"Africa","contPt":"África"},"sd":{"nameEn":"Sudan","namePt":"Sudão","contEn":"Africa","contPt":"África"},"se":{"nameEn":"Sweden","namePt":"Suécia","contEn":"Europe","contPt":"Europa"},"sg":{"nameEn":"Singapore","namePt":"Singapura","contEn":"Asia","contPt":"Ásia"},"si":{"nameEn":"Slovenia","namePt":"Eslovénia","contEn":"Europe","contPt":"Europa"},"sk":{"nameEn":"Slovakia","namePt":"Eslováquia","contEn":"Europe","contPt":"Europa"},"sl":{"nameEn":"Sierra Leone","namePt":"Serra Leoa","contEn":"Africa","contPt":"África"},"sm":{"nameEn":"San Marino","namePt":"São Marino","contEn":"Europe","contPt":"Europa"},"sn":{"nameEn":"Senegal","namePt":"Senegal","contEn":"Africa","contPt":"África"},"so":{"nameEn":"Somalia","namePt":"Somália","contEn":"Africa","contPt":"África"},"sr":{"nameEn":"Suriname","namePt":"Suriname","contEn":"South America","contPt":"América do Sul"},"ss":{"nameEn":"South Sudan","namePt":"Sudão do Sul","contEn":"Africa","contPt":"África"},"st":{"nameEn":"São Tomé and Príncipe","namePt":"São Tomé e Príncipe","contEn":"Africa","contPt":"África"},"sv":{"nameEn":"El Salvador","namePt":"El Salvador","contEn":"North America","contPt":"América do Norte"},"sy":{"nameEn":"Syria","namePt":"Síria","contEn":"Asia","contPt":"Ásia"},"sz":{"nameEn":"Eswatini","namePt":"Essuatíni","contEn":"Africa","contPt":"África"},"td":{"nameEn":"Chad","namePt":"Chade","contEn":"Africa","contPt":"África"},"tg":{"nameEn":"Togo","namePt":"Togo","contEn":"Africa","contPt":"África"},"th":{"nameEn":"Thailand","namePt":"Tailândia","contEn":"Asia","contPt":"Ásia"},"tj":{"nameEn":"Tajikistan","namePt":"Tajiquistão","contEn":"Asia","contPt":"Ásia"},"tl":{"nameEn":"Timor-Leste","namePt":"Timor-Leste","contEn":"Asia","contPt":"Ásia"},"tm":{"nameEn":"Turkmenistan","namePt":"Turquemenistão","contEn":"Asia","contPt":"Ásia"},"tn":{"nameEn":"Tunisia","namePt":"Tunísia","contEn":"Africa","contPt":"África"},"to":{"nameEn":"Tonga","namePt":"Tonga","contEn":"Oceania","contPt":"Oceânia"},"tr":{"nameEn":"Turkey","namePt":"Turquia","contEn":"Asia","contPt":"Ásia"},"tt":{"nameEn":"Trinidad and Tobago","namePt":"Trindade e Tobago","contEn":"North America","contPt":"América do Norte"},"tv":{"nameEn":"Tuvalu","namePt":"Tuvalu","contEn":"Oceania","contPt":"Oceânia"},"tw":{"nameEn":"Taiwan","namePt":"Taiwan","contEn":"Asia","contPt":"Ásia"},"tz":{"nameEn":"Tanzania","namePt":"Tanzânia","contEn":"Africa","contPt":"África"},"ua":{"nameEn":"Ukraine","namePt":"Ucrânia","contEn":"Europe","contPt":"Europa"},"ug":{"nameEn":"Uganda","namePt":"Uganda","contEn":"Africa","contPt":"África"},"us":{"nameEn":"United States","namePt":"Estados Unidos","contEn":"North America","contPt":"América do Norte"},"uy":{"nameEn":"Uruguay","namePt":"Uruguai","contEn":"South America","contPt":"América do Sul"},"uz":{"nameEn":"Uzbekistan","namePt":"Usbequistão","contEn":"Asia","contPt":"Ásia"},"va":{"nameEn":"Vatican City","namePt":"Vaticano","contEn":"Europe","contPt":"Europa"},"vc":{"nameEn":"St Vincent and the Grenadines","namePt":"São Vicente e Granadinas","contEn":"North America","contPt":"América do Norte"},"ve":{"nameEn":"Venezuela","namePt":"Venezuela","contEn":"South America","contPt":"América do Sul"},"vn":{"nameEn":"Vietnam","namePt":"Vietname","contEn":"Asia","contPt":"Ásia"},"vu":{"nameEn":"Vanuatu","namePt":"Vanuatu","contEn":"Oceania","contPt":"Oceânia"},"ws":{"nameEn":"Samoa","namePt":"Samoa","contEn":"Oceania","contPt":"Oceânia"},"ye":{"nameEn":"Yemen","namePt":"Iémen","contEn":"Asia","contPt":"Ásia"},"za":{"nameEn":"South Africa","namePt":"África do Sul","contEn":"Africa","contPt":"África"},"zm":{"nameEn":"Zambia","namePt":"Zâmbia","contEn":"Africa","contPt":"África"},"zw":{"nameEn":"Zimbabwe","namePt":"Zimbabué","contEn":"Africa","contPt":"África"},"pr":{"nameEn":"Puerto Rico","namePt":"Porto Rico","contEn":"North America","contPt":"América do Norte"},"gl":{"nameEn":"Greenland","namePt":"Gronelândia","contEn":"North America","contPt":"América do Norte"},"fk":{"nameEn":"Falkland Islands","namePt":"Ilhas Falkland","contEn":"South America","contPt":"América do Sul"},"eh":{"nameEn":"Western Sahara","namePt":"Sahara Ocidental","contEn":"Africa","contPt":"África"},"xk":{"nameEn":"Kosovo","namePt":"Kosovo","contEn":"Europe","contPt":"Europa"},"nc":{"nameEn":"New Caledonia","namePt":"Nova Caledónia","contEn":"Oceania","contPt":"Oceânia"},"tf":{"nameEn":"French Southern Territories","namePt":"Território Francês do Sul","contEn":"Africa","contPt":"África"},"aq":{"nameEn":"Antarctica","namePt":"Antártida","contEn":"Oceania","contPt":"Oceânia"}};
const ID_TO_ISO2 = {"botswana":"bw","cabo-verde":"cv","egypt":"eg","kenya":"ke","mauritius":"mu","morocco":"ma","namibia":"na","south-africa":"za","tanzania":"tz","tn":"tn","zambia":"zm","zimbabwe":"zw","cambodia":"kh","china":"cn","india":"in","indonesia":"id","japan":"jp","jo":"jo","kuwait":"kw","laos":"la","malaysia":"my","np":"np","oman":"om","ph":"ph","qatar":"qa","singapore":"sg","kr":"kr","lk":"lk","thailand":"th","uae":"ae","vietnam":"vn","austria":"at","belgium":"be","bosnia":"ba","croatia":"hr","czech-republic":"cz","denmark":"dk","france":"fr","georgia":"ge","germany":"de","greece":"gr","iceland":"is","ireland":"ie","italy":"it","liechtenstein":"li","lt":"lt","luxembourg":"lu","mt":"mt","monaco":"mc","netherlands":"nl","north-macedonia":"mk","norway":"no","poland":"pl","portugal":"pt","ro":"ro","san-marino":"sm","serbia":"rs","slovakia":"sk","spain":"es","sweden":"se","switzerland":"ch","turkey":"tr","uk":"gb","vatican":"va","belize":"bz","canada":"ca","costa-rica":"cr","mexico":"mx","panama":"pa","usa":"us","argentina":"ar","bolivia":"bo","brazil":"br","chile":"cl","colombia":"co","ecuador":"ec","peru":"pe","uy":"uy","australia":"au","fiji":"fj","new-zealand":"nz","vanuatu":"vu","hu":"hu","ee":"ee","fi":"fi","bs":"bs","tw":"tw","mn":"mn","et":"et","uz":"uz","bg":"bg","lv":"lv","kz":"kz","bt":"bt","am":"am","rw":"rw","ng":"ng","jm":"jm","do":"do","sa":"sa"};

function ContinentIcon({ id, size = 28 }) {
  const stroke = "currentColor";
  const common = { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke, strokeWidth: 1.6 };
  if (id === "europe") return <svg {...common}><path d="M6 20 V12 Q6 5 12 4 Q18 5 18 12 V20" /><path d="M6 20 H18" /></svg>;
  if (id === "asia") return <svg {...common}><path d="M4 20 V8 M20 20 V8" /><path d="M2 8 L22 8" /><path d="M4 11.5 L20 11.5" /></svg>;
  if (id === "africa") return <svg {...common}><circle cx="12" cy="11" r="4.5" /><path d="M12 3 V5.5 M4.5 7 L6.3 8.5 M19.5 7 L17.7 8.5" /><path d="M3 19 H21" /></svg>;
  if (id === "north-america") return <svg {...common}><path d="M2 20 V15 H6 V11 H11 V16 H15 V12 H22 V20 Z" /></svg>;
  if (id === "south-america") return <svg {...common}><path d="M12 4 L19 20 H5 Z" /><circle cx="12" cy="9" r="1.5" fill={stroke} stroke="none" /></svg>;
  if (id === "oceania") return <svg {...common}><path d="M2 15 Q 6 11 10 15 T 18 15 T 22 15" /><path d="M2 19 Q 6 15 10 19 T 18 19 T 22 19" /><circle cx="17" cy="7" r="3" /></svg>;
  return null;
}

function Waypoint() {
  const [view, setView] = useState("continents");
  const [continentId, setContinentId] = useState(null);
  const [countryId, setCountryId] = useState(null);
  const [countryDataCache, setCountryDataCache] = useState({});
  // Heavy per-country content (attractions, itinerary, food, FAQ...) is split into
  // its own JSON file per country and fetched lazily on demand — see split_data.py.
  // This is why index.html only ships ~450KB instead of >1MB for 100 countries.
  // Retries twice with backoff before surfacing a real error state (see
  // countryDetailError / __error_<id> below), instead of failing silently on a
  // flaky connection.
  const ensureCountryData = (id, attempt) => {
    attempt = attempt || 0;
    if (!id || countryDataCache[id] || countryDataCache["__loading_" + id]) return;
    setCountryDataCache((c) => { const n = { ...c, ["__loading_" + id]: true }; delete n["__error_" + id]; return n; });
    fetch("countries-data/" + id + ".json")
      .then((r) => { if (!r.ok) throw new Error("not found"); return r.json(); })
      .then((data) => setCountryDataCache((c) => { const n = { ...c, [id]: data }; delete n["__loading_" + id]; delete n["__error_" + id]; return n; }))
      .catch(() => {
        if (attempt < 2) {
          setCountryDataCache((c) => { const n = { ...c }; delete n["__loading_" + id]; return n; });
          setTimeout(() => ensureCountryData(id, attempt + 1), 800 * (attempt + 1));
        } else {
          setCountryDataCache((c) => { const n = { ...c }; delete n["__loading_" + id]; n["__error_" + id] = true; return n; });
        }
      });
  };
  const withFullData = (cty) => {
    if (!cty) return cty;
    const full = countryDataCache[cty.id];
    if (!full) return cty;
    const merged = { ...cty, ...full };
    if (full.pt || cty.pt) merged.pt = { ...(cty.pt || {}), ...(full.pt || {}) };
    return merged;
  };
  const [lang, setLang] = useState("en");
  const [homeQuery, setHomeQuery] = useState("");
  const [mapQuery, setMapQuery] = useState("");
  const [continentQuery, setContinentQuery] = useState("");
  const [quizStarted, setQuizStarted] = useState(false);
  const [quizIndex, setQuizIndex] = useState(0);
  const [quizScore, setQuizScore] = useState(0);
  const [quizSelected, setQuizSelected] = useState(null);
  const [quizFinished, setQuizFinished] = useState(false);
  const [quizCopied, setQuizCopied] = useState(false);

  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);
  const [showAuthModal, setShowAuthModal] = useState(false);
  const [authMode, setAuthMode] = useState("signin");
  const [showNewsletterNudge, setShowNewsletterNudge] = useState(false);
  const [authEmail, setAuthEmail] = useState("");
  const [authPassword, setAuthPassword] = useState("");
  const [authError, setAuthError] = useState("");
  const [authBusy, setAuthBusy] = useState(false);
  const [countryStatuses, setCountryStatuses] = useState({});
  const [visitedLog, setVisitedLog] = useState([]);
  const [popoverCountry, setPopoverCountry] = useState(null);
  const [cameFromMap, setCameFromMap] = useState(false);
  const mapDivRef = useRef(null);
  const leafletMapRef = useRef(null);
  const mapLayersRef = useRef({});
  const [trips, setTrips] = useState({});
  const [activeTripId, setActiveTripId] = useState(null);
  const [openAccordion, setOpenAccordion] = useState({});
  const toggleAccordion = (key) => setOpenAccordion((p) => ({ ...p, [key]: !p[key] }));
  const [activeDetailSection, setActiveDetailSection] = useState("essential");
  const detailSectionRefs = useRef({});
  const scrollToDetailSection = (id) => {
    const el = detailSectionRefs.current[id];
    if (el) {
      const y = el.getBoundingClientRect().top + window.pageYOffset - 96;
      const reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: y, behavior: reduceMotion ? "auto" : "smooth" });
    }
  };
  const [showNewTripForm, setShowNewTripForm] = useState(false);
  const [newTripName, setNewTripName] = useState("");
  const [newTripCountryQuery, setNewTripCountryQuery] = useState("");
  const [newTripCountryId, setNewTripCountryId] = useState(null);
  const [newTripStart, setNewTripStart] = useState("");
  const [newTripEnd, setNewTripEnd] = useState("");
  const [highlightDrafts, setHighlightDrafts] = useState({});
  const [stayDrafts, setStayDrafts] = useState({});
  const [mealDrafts, setMealDrafts] = useState({});
  const [tripSaveStatus, setTripSaveStatus] = useState("");
  // Only one "Places / Where to sleep / Where to eat / Transport" panel can be open
  // across the whole trip at a time (bottom sheet on mobile, modal on desktop — see
  // .wp-task-sheet-*). Storing a single {stopId, type} instead of a per-button
  // open/closed flag is what guarantees that opening a new panel always closes
  // whichever one was open before, per the approved design decision.
  const [activeEditPanel, setActiveEditPanel] = useState(null);
  const editPanelRef = useRef(null);
  const editPanelTriggerRef = useRef(null);
  const openEditPanel = (stopId, type, triggerEl) => {
    setActiveEditPanel((cur) => (cur && cur.stopId === stopId && cur.type === type) ? null : { stopId, type });
    if (triggerEl) editPanelTriggerRef.current = triggerEl;
  };
  const closeEditPanel = () => setActiveEditPanel(null);
  useEffect(() => {
    if (!activeEditPanel) return;
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    const onKeyDown = (e) => {
      if (e.key === "Escape") { closeEditPanel(); return; }
      if (e.key === "Tab" && editPanelRef.current) {
        const focusable = editPanelRef.current.querySelectorAll('button, a, input, select, [tabindex]:not([tabindex="-1"])');
        if (focusable.length === 0) return;
        const first = focusable[0], last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    };
    document.addEventListener("keydown", onKeyDown);
    if (editPanelRef.current) { const first = editPanelRef.current.querySelector('input, button'); if (first) first.focus(); }
    return () => {
      document.body.style.overflow = prevOverflow;
      document.removeEventListener("keydown", onKeyDown);
      if (editPanelTriggerRef.current) editPanelTriggerRef.current.focus();
    };
  }, [activeEditPanel]);

  const [activeTripTab, setActiveTripTab] = useState("route");
  const [bookingsSubTab, setBookingsSubTab] = useState("all");
  const [documentDraft, setDocumentDraft] = useState("");
  const [selectedDay, setSelectedDay] = useState(1);
  const [dayView, setDayView] = useState("list");
  const [activityDrafts, setActivityDrafts] = useState({});
  useEffect(() => { if (view === "trip-detail") { setActiveTripTab("route"); setSelectedDay(1); } }, [view, activeTripId]);

  const [geocodeCache, setGeocodeCache] = useState({});
  const geocodeCity = (query, countryName) => {
    const key = (query + "|" + (countryName || "")).toLowerCase();
    if (!query || geocodeCache[key]) return;
    setGeocodeCache((c) => ({ ...c, [key]: "loading" }));
    const q = encodeURIComponent(query + (countryName ? ", " + countryName : ""));
    fetch("https://nominatim.openstreetmap.org/search?format=json&limit=1&q=" + q)
      .then((r) => r.json())
      .then((results) => {
        const hit = results && results[0];
        setGeocodeCache((c) => ({ ...c, [key]: hit ? { lat: parseFloat(hit.lat), lng: parseFloat(hit.lon) } : null }));
      })
      .catch(() => setGeocodeCache((c) => ({ ...c, [key]: null })));
  };
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const menuTriggerRef = useRef(null);
  const menuPanelRef = useRef(null);
  useEffect(() => {
    if (!mobileMenuOpen) return;
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    const onKeyDown = (e) => {
      if (e.key === "Escape") { setMobileMenuOpen(false); return; }
      if (e.key === "Tab" && menuPanelRef.current) {
        const focusable = menuPanelRef.current.querySelectorAll('button, a, [tabindex]:not([tabindex="-1"])');
        if (focusable.length === 0) return;
        const first = focusable[0], last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    };
    document.addEventListener("keydown", onKeyDown);
    if (menuPanelRef.current) { const first = menuPanelRef.current.querySelector('button, a'); if (first) first.focus(); }
    return () => {
      document.body.style.overflow = prevOverflow;
      document.removeEventListener("keydown", onKeyDown);
      if (menuTriggerRef.current) menuTriggerRef.current.focus();
    };
  }, [mobileMenuOpen]);
  const [shareCopied, setShareCopied] = useState(false);
  const [editingNoteDay, setEditingNoteDay] = useState(null);
  const [sharedTrip, setSharedTrip] = useState(null);
  const [sharedTripStatus, setSharedTripStatus] = useState("idle");

  const normalize = (s) => (s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  const T = UI_STRINGS[lang];
  const continents = CONTINENTS.map((c) => localizeContinent(c, lang));
  const continent = continents.find((c) => c.id === continentId) || null;
  const country = withFullData(continent ? continent.countries.find((c) => c.id === countryId) : null);

  useEffect(() => {
    if (view !== "detail") return;
    const onScroll = () => {
      const ids = ["essential", "places", "food", "route", "faq"];
      let current = ids[0];
      for (const id of ids) {
        const el = detailSectionRefs.current[id];
        if (el && el.getBoundingClientRect().top - 110 <= 0) current = id;
      }
      setActiveDetailSection(current);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, [view, country && country.id]);

  useEffect(() => {
    if (view === "detail" && countryId) ensureCountryData(countryId);
    if (view === "trip-detail" && activeTripId && trips[activeTripId]) ensureCountryData(trips[activeTripId].countryId);
  }, [view, countryId, activeTripId]);

  const setHash = (h) => {
    const newHash = h ? "#" + h : "";
    if (window.location.hash !== newHash) {
      const base = window.location.pathname + window.location.search;
      history.pushState(null, "", h ? base + newHash : base);
    }
  };

  const goToContinents = () => { setView("continents"); setContinentId(null); setCountryId(null); setHomeQuery(""); setHash(""); };
  const goToCountries = (cId) => { setContinentId(cId); setCountryId(null); setView("countries"); setContinentQuery(""); window.scrollTo(0, 0); setHash("continent=" + cId); };
  const goToDetail = (cty) => { setCountryId(cty.id); setView("detail"); window.scrollTo(0, 0); setHash("country=" + cty.id); };
  const goToDetailFromSearch = (cty) => { if (cty.isExtra) return; setCameFromMap(false); setContinentId(cty.continentId); setCountryId(cty.id); setView("detail"); setHomeQuery(""); window.scrollTo(0, 0); setHash("country=" + cty.id); };
  const goToStatic = (page) => { setView(page); setContinentId(null); setCountryId(null); window.scrollTo(0, 0); setHash(page); };

  const allCountriesFlat = continents.flatMap((c) => c.countries.map((cty) => withFullData({ ...cty, continentId: c.id, continentName: c.name, continentColor: c.color })));
  const isoToFlag = (iso) => iso.toUpperCase().replace(/./g, (ch) => String.fromCodePoint(127397 + ch.charCodeAt(0)));
  const allCountriesForMap = allCountriesFlat.concat(
    Object.keys(WORLD_MAP_META).filter((key) => !Object.values(ID_TO_ISO2).includes(key)).map((key) => {
      const m = WORLD_MAP_META[key];
      return {
        id: key,
        name: lang === "pt" ? m.namePt : m.nameEn,
        continentName: lang === "pt" ? m.contPt : m.contEn,
        flag: isoToFlag(key),
        capital: "",
        isExtra: true,
      };
    })
  );
  const totalAttractions = 600; // precomputed: 100 countries x 6 attractions each, doesn't depend on lazy-loaded detail data
  const currentMonth = new Date().getMonth() + 1;
  const nowPicks = (WHERE_TO_GO_NOW[currentMonth] || [])
    .map((pick) => {
      const found = allCountriesFlat.find((c) => c.id === pick.id);
      if (!found) return null;
      return { ...found, reason: pick.reason[lang] || pick.reason.en };
    })
    .filter(Boolean);

  // --- Passport Quiz: deterministic per month, same for every visitor ---
  const seededRandom = (seed) => {
    let t = seed += 0x6D2B79F5;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const seededShuffle = (arr, seed) => {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(seededRandom(seed + i) * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };
  const CLUE_ORDER = ["tagline", "highlight", "food", "flag"];
  const buildClueCandidates = (cty) => {
    const nameNorm = normalize(cty.name);
    const candidates = [];
    if (cty.tagline && !normalize(cty.tagline).includes(nameNorm)) {
      candidates.push({ type: "tagline", text: cty.tagline });
    }
    if (cty.highlights && cty.highlights.length) {
      const h = cty.highlights.find((h) => !normalize(h).includes(nameNorm));
      if (h) candidates.push({ type: "highlight", text: h });
    }
    if (cty.food && cty.food.length) {
      const f = cty.food.find((f) => !normalize(f.name).includes(nameNorm) && !normalize(f.desc || "").includes(nameNorm));
      if (f) candidates.push({ type: "food", text: f.name + " — " + f.desc });
    }
    candidates.push({ type: "flag", text: null });
    return candidates;
  };
  const quizCountryIds = MONTHLY_QUIZ[currentMonth] || [];

  useEffect(() => {
    quizCountryIds.forEach((id) => ensureCountryData(id));
    // eslint-disable-next-line
  }, []);
  const quizQuestions = quizCountryIds.map((id, i) => {
    const country = allCountriesFlat.find((c) => c.id === id);
    if (!country) return null;
    const candidates = buildClueCandidates(country);
    const preferredType = CLUE_ORDER[i % 4];
    const clue = candidates.find((c) => c.type === preferredType) || candidates[0];
    const wrongPool = allCountriesFlat.filter((c) => c.id !== country.id && !quizCountryIds.includes(c.id));
    const distractors = seededShuffle(wrongPool, currentMonth * 1000 + i).slice(0, 3);
    const options = seededShuffle([country, ...distractors], currentMonth * 1000 + i + 500);
    return { country, clue, options, correctId: country.id };
  }).filter(Boolean);

  const quizPromptFor = (type) => {
    if (type === "tagline") return T.quizPromptTagline;
    if (type === "highlight") return T.quizPromptHighlight;
    if (type === "food") return T.quizPromptFood;
    return T.quizPromptFlag;
  };

  const startQuiz = () => { setQuizStarted(true); setQuizIndex(0); setQuizScore(0); setQuizSelected(null); setQuizFinished(false); setQuizCopied(false); };
  const answerQuiz = (optionId) => {
    if (quizSelected) return;
    setQuizSelected(optionId);
    if (optionId === quizQuestions[quizIndex].correctId) setQuizScore((s) => s + 1);
  };
  const nextQuizQuestion = () => {
    if (quizIndex + 1 >= quizQuestions.length) { setQuizFinished(true); }
    else { setQuizIndex((i) => i + 1); setQuizSelected(null); }
  };
  const quizRank = (score) => {
    if (score <= 2) return T.quizRank0;
    if (score <= 5) return T.quizRank1;
    if (score <= 7) return T.quizRank2;
    return T.quizRank3;
  };
  const copyQuizResult = () => {
    const text = T.quizShareText.replace("SCORE", String(quizScore));
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => { setQuizCopied(true); setTimeout(() => setQuizCopied(false), 2000); });
    }
  };

  const homeSearchResults = homeQuery.trim()
    ? allCountriesFlat.filter((cty) => normalize(cty.name).includes(normalize(homeQuery)) || normalize(cty.capital).includes(normalize(homeQuery)))
    : [];
  const mapSearchResults = mapQuery.trim()
    ? allCountriesForMap.filter((cty) => normalize(cty.name).includes(normalize(mapQuery)) || normalize(cty.capital || "").includes(normalize(mapQuery)))
    : [];
  const groupCountriesByContinent = (list) => {
    const groups = {};
    list.forEach((cty) => {
      if (!groups[cty.continentName]) groups[cty.continentName] = [];
      groups[cty.continentName].push(cty);
    });
    return groups;
  };
  const mapVisitedCountries = allCountriesForMap.filter((cty) => countryStatuses[cty.id] === "visited");
  const mapWantCountries = allCountriesForMap.filter((cty) => countryStatuses[cty.id] === "want");
  const mapVisitedByContinent = groupCountriesByContinent(mapVisitedCountries);
  const mapWantByContinent = groupCountriesByContinent(mapWantCountries);
  const continentSearchResults = continent && continentQuery.trim()
    ? continent.countries.filter((cty) => normalize(cty.name).includes(normalize(continentQuery)) || normalize(cty.capital).includes(normalize(continentQuery)))
    : (continent ? continent.countries : []);

  const goToCountryById = (id) => {
    for (const cont of continents) {
      const found = cont.countries.find((c) => c.id === id);
      if (found) { setContinentId(cont.id); setCountryId(found.id); setView("detail"); window.scrollTo(0, 0); setHash("country=" + id); return; }
    }
  };

  const applyHashState = (hash) => {
    if (!hash) { goToContinents(); return; }
    if (hash.startsWith("country=")) { goToCountryById(hash.split("=")[1]); return; }
    if (hash.startsWith("continent=")) { goToCountries(hash.split("=")[1]); return; }
    if (hash.startsWith("shared=")) { loadSharedTrip(hash.split("=")[1]); return; }
    if (["about", "newsletter", "articles", "products", "map"].includes(hash)) { goToStatic(hash); return; }
  };

  useEffect(() => {
    applyHashState(window.location.hash.replace("#", ""));
    const onHashChange = () => applyHashState(window.location.hash.replace("#", ""));
    window.addEventListener("hashchange", onHashChange);
    window.addEventListener("popstate", onHashChange);
    return () => {
      window.removeEventListener("hashchange", onHashChange);
      window.removeEventListener("popstate", onHashChange);
    };
  }, []);

  const firebaseReady = typeof window !== "undefined" && window.firebase && window.firebase.apps && window.firebase.apps.length > 0;

  useEffect(() => {
    if (!firebaseReady) { setAuthLoading(false); return; }
    const unsub = firebase.auth().onAuthStateChanged((u) => {
      setUser(u);
      setAuthLoading(false);
      if (u) {
        firebase.firestore().collection("users").doc(u.uid).get()
          .then((doc) => {
            const data = doc.exists ? doc.data() : {};
            setCountryStatuses(data.countries || {});
            setTrips(data.trips || {});
            setVisitedLog(data.visitedLog || []);
          })
          .catch(() => { setCountryStatuses({}); setTrips({}); setVisitedLog([]); });
      } else {
        setCountryStatuses({});
        setTrips({});
        setVisitedLog([]);
      }
    });
    return () => unsub();
  }, [firebaseReady]);

  const openAuthModal = (mode) => { setAuthMode(mode || "signin"); setAuthError(""); setAuthEmail(""); setAuthPassword(""); setShowAuthModal(true); };
  const closeAuthModal = () => { setShowAuthModal(false); setAuthError(""); setAuthBusy(false); setShowNewsletterNudge(false); };

  const signInWithGoogle = () => {
    if (!firebaseReady) return;
    setAuthError(""); setAuthBusy(true);
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
      .then((result) => {
        setAuthBusy(false);
        if (result && result.additionalUserInfo && result.additionalUserInfo.isNewUser) {
          setShowNewsletterNudge(true);
        } else {
          closeAuthModal();
        }
      })
      .catch((e) => { setAuthError(e.message); setAuthBusy(false); });
  };
  const submitAuthForm = () => {
    if (!firebaseReady) return;
    setAuthError(""); setAuthBusy(true);
    const wasSignup = authMode === "signup";
    const action = wasSignup
      ? firebase.auth().createUserWithEmailAndPassword(authEmail, authPassword)
      : firebase.auth().signInWithEmailAndPassword(authEmail, authPassword);
    action.then(() => {
      setAuthBusy(false);
      if (wasSignup) setShowNewsletterNudge(true); else closeAuthModal();
    }).catch((e) => { setAuthError(e.message); setAuthBusy(false); });
  };
  const signOutUser = () => { setShowUserMenu(false); if (firebaseReady) firebase.auth().signOut(); };

  const setCountryStatus = (countryId, status) => {
    if (!user) { openAuthModal("signin"); return; }
    const next = { ...countryStatuses };
    const wasVisited = next[countryId] === "visited";
    if (!status || next[countryId] === status) delete next[countryId];
    else next[countryId] = status;
    setCountryStatuses(next);
    const isNowVisited = next[countryId] === "visited";
    let nextLog = visitedLog;
    if (isNowVisited && !wasVisited) {
      nextLog = [...visitedLog.filter((l) => l.id !== countryId), { id: countryId, date: new Date().toISOString() }];
      setVisitedLog(nextLog);
    } else if (!isNowVisited && wasVisited) {
      nextLog = visitedLog.filter((l) => l.id !== countryId);
      setVisitedLog(nextLog);
    }
    firebase.firestore().collection("users").doc(user.uid).set({ countries: next, visitedLog: nextLog }, { merge: true }).catch(() => {});
  };

  const goToDetailFromMap = (cty) => {
    if (!cty) return;
    if (cty.isExtra) { setPopoverCountry(cty); return; }
    goToDetailFromSearch(cty);
    setCameFromMap(true);
  };

  const backFromDetail = () => {
    if (cameFromMap) { setCameFromMap(false); goToStatic("map"); }
    else { goToCountries(continentId); }
  };

  const [mapDataReady, setMapDataReady] = useState(typeof window !== "undefined" && !!window.WORLD_MAP_CONTOURS);
  const [mapDataError, setMapDataError] = useState(false);
  const loadMapData = () => {
    if (window.WORLD_MAP_CONTOURS) { setMapDataReady(true); return; }
    if (!window.__wpMapDataPromise) {
      window.__wpMapDataPromise = new Promise((resolve, reject) => {
        const s = document.createElement("script");
        s.src = "map-data.js";
        s.onload = resolve;
        s.onerror = reject;
        document.body.appendChild(s);
      });
    }
    window.__wpMapDataPromise
      .then(() => { setMapDataReady(true); setMapDataError(false); })
      .catch(() => { window.__wpMapDataPromise = null; setMapDataError(true); });
  };
  const retryMapData = () => { setMapDataError(false); loadMapData(); };

  const ISO2_TO_ID = {};
  Object.keys(ID_TO_ISO2).forEach((id) => { ISO2_TO_ID[ID_TO_ISO2[id]] = id; });
  const idForIso2 = (iso2) => ISO2_TO_ID[iso2] || iso2;
  const ctyForIso2 = (iso2) => allCountriesForMap.find((c) => c.id === idForIso2(iso2));
  const mapStyleForIso2 = (iso2) => {
    const id = idForIso2(iso2);
    const status = countryStatuses[id];
    const hasPage = !!ISO2_TO_ID[iso2];
    const fillColor = status === "visited" ? "#3F8F6F" : status === "want" ? "#3E7CB1" : (hasPage ? "#FFFFFF" : "#EDE6D4");
    return { fillColor, fillOpacity: 0.92, color: "#E3E8EF", weight: 0.8 };
  };
  const mapClickHandlerRef = useRef(null);
  mapClickHandlerRef.current = (cty) => goToDetailFromMap(cty);

  useEffect(() => {
    if (view !== "map") return;
    if (!mapDataReady) { loadMapData(); return; }
    if (!mapDivRef.current || typeof window.L === "undefined") return;
    const L = window.L;
    const map = L.map(mapDivRef.current, {
      center: [20, 12], zoom: 2, minZoom: 2, maxZoom: 7, zoomControl: false,
      worldCopyJump: false, maxBounds: [[-89, -200], [89, 200]], maxBoundsViscosity: 0.9,
    });
    leafletMapRef.current = map;
    L.control.zoom({ position: "bottomright" }).addTo(map);

    const features = Object.keys(window.WORLD_MAP_CONTOURS).map((iso2) => ({
      type: "Feature", properties: { iso2 }, geometry: window.WORLD_MAP_CONTOURS[iso2],
    }));
    const geoLayer = L.geoJSON({ type: "FeatureCollection", features }, {
      style: (feature) => mapStyleForIso2(feature.properties.iso2),
      onEachFeature: (feature, layer) => {
        const iso2 = feature.properties.iso2;
        mapLayersRef.current[iso2] = layer;
        layer.on({
          mouseover: () => { layer.setStyle({ weight: 1.8 }); layer.bringToFront(); },
          mouseout: () => { layer.setStyle({ weight: 0.8 }); },
          click: () => { mapClickHandlerRef.current(ctyForIso2(iso2)); },
        });
      },
    }).addTo(map);
    setTimeout(() => { map.invalidateSize(); }, 0);

    Object.keys(window.WORLD_MAP_POINTS).forEach((iso2) => {
      const p = window.WORLD_MAP_POINTS[iso2];
      const s = mapStyleForIso2(iso2);
      const marker = L.circleMarker([p.lat, p.lng], { radius: 5, fillColor: s.fillColor, fillOpacity: 0.92, color: s.color, weight: 1 }).addTo(map);
      mapLayersRef.current[iso2] = marker;
      marker.on({ click: () => { mapClickHandlerRef.current(ctyForIso2(iso2)); } });
    });

    return () => { map.remove(); leafletMapRef.current = null; mapLayersRef.current = {}; };
  }, [view, mapDataReady]);

  useEffect(() => {
    if (!leafletMapRef.current) return;
    Object.keys(mapLayersRef.current).forEach((iso2) => {
      mapLayersRef.current[iso2].setStyle(mapStyleForIso2(iso2));
    });
  }, [countryStatuses, lang]);

  const handleMapCountryClick = (cty) => goToDetailFromMap(cty);

  const pctVisited = allCountriesForMap.length ? Math.round((countryStatuses && Object.values(countryStatuses).filter((s) => s === "visited").length) / allCountriesForMap.length * 100) : 0;

  const visitedSparkline = (() => {
    if (visitedLog.length < 2) return null;
    const sorted = [...visitedLog].sort((a, b) => new Date(a.date) - new Date(b.date));
    const w = 220, h = 46, pad = 3;
    const maxY = sorted.length;
    const pts = sorted.map((entry, i) => {
      const x = pad + (i / (sorted.length - 1)) * (w - pad * 2);
      const y = h - pad - ((i + 1) / maxY) * (h - pad * 2);
      return x.toFixed(1) + "," + y.toFixed(1);
    });
    return { d: "M" + pts.join(" L"), w, h };
  })();


  const saveTrips = (next) => {
    setTrips(next);
    if (user) firebase.firestore().collection("users").doc(user.uid).set({ trips: next }, { merge: true }).catch(() => {});
  };

  const saveTripNow = (tripId) => {
    saveTrips({ ...trips });
    const savedTrip = trips[tripId];
    if (savedTrip) syncSharedSnapshot(savedTrip);
    setTripSaveStatus("saved");
    setTimeout(() => setTripSaveStatus(""), 1800);
  };

  const updateDailyNote = (tripId, day, text) => {
    updateTrip(tripId, (t) => ({ ...t, dailyNotes: { ...(t.dailyNotes || {}), [day]: text } }));
  };

  const generateShareId = () => (Math.random().toString(36).slice(2, 8) + Date.now().toString(36)).slice(0, 12);

  const buildShareSnapshot = (trip) => ({
    name: trip.name,
    countryId: trip.countryId,
    countryName: trip.countryName,
    flag: trip.flag,
    startDate: trip.startDate,
    endDate: trip.endDate,
    stops: trip.stops,
    transits: trip.transits,
    dailyNotes: trip.dailyNotes || {},
    ownerUid: user ? user.uid : null,
    updatedAt: new Date().toISOString(),
  });

  const syncSharedSnapshot = (trip) => {
    if (!trip || !trip.isPublic || !trip.shareId || !firebaseReady || !user) return;
    firebase.firestore().collection("shared_trips").doc(trip.shareId).set(buildShareSnapshot(trip)).catch(() => {});
  };

  const toggleTripPublic = (trip) => {
    if (!user || !firebaseReady) return;
    if (trip.isPublic) {
      if (trip.shareId) {
        firebase.firestore().collection("shared_trips").doc(trip.shareId).delete().catch(() => {});
      }
      updateTrip(trip.id, (t) => ({ ...t, isPublic: false }));
    } else {
      const shareId = trip.shareId || generateShareId();
      firebase.firestore().collection("shared_trips").doc(shareId).set(buildShareSnapshot({ ...trip, shareId })).catch(() => {});
      updateTrip(trip.id, (t) => ({ ...t, isPublic: true, shareId }));
    }
  };

  const copyShareLink = (shareId) => {
    const url = window.location.origin + window.location.pathname + "#shared=" + shareId;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => { setShareCopied(true); setTimeout(() => setShareCopied(false), 2000); });
    }
  };

  const loadSharedTrip = (shareId) => {
    setView("shared-trip");
    setSharedTripStatus("loading");
    setSharedTrip(null);
    if (!firebaseReady) { setSharedTripStatus("error"); return; }
    firebase.firestore().collection("shared_trips").doc(shareId).get()
      .then((doc) => {
        if (doc.exists) { setSharedTrip(doc.data()); setSharedTripStatus("ready"); }
        else { setSharedTripStatus("error"); }
      })
      .catch(() => setSharedTripStatus("error"));
  };

  const dayCount = (start, end) => {
    if (!start || !end) return 1;
    const diff = Math.round((new Date(end) - new Date(start)) / 86400000) + 1;
    return diff > 0 ? diff : 1;
  };

  const toISODate = (d) => d.toISOString().slice(0, 10);
  const truncateSummary = (text, maxLen) => {
    if (!text || text.length <= maxLen) return text;
    const firstSentence = text.split(/(?<=[.!?])\s/)[0];
    if (firstSentence && firstSentence.length <= maxLen) return firstSentence;
    const cut = text.slice(0, maxLen);
    return cut.slice(0, cut.lastIndexOf(" ")) + "…";
  };
  const formatDayRange = (trip, dayStart, dayEnd) => {
    if (!trip.startDate || !dayStart || !dayEnd) return "";
    const start = new Date(new Date(trip.startDate).getTime() + (dayStart - 1) * 86400000);
    const end = new Date(new Date(trip.startDate).getTime() + (dayEnd - 1) * 86400000);
    const locale = lang === "pt" ? "pt-PT" : "en-GB";
    const opts = { day: "numeric", month: "short" };
    return start.toLocaleDateString(locale, opts) + " – " + end.toLocaleDateString(locale, opts);
  };
  const openNewTripForm = () => {
    if (!user) { openAuthModal("signin"); return; }
    const today = new Date();
    const weekLater = new Date(today.getTime() + 7 * 86400000);
    setNewTripName(""); setNewTripCountryQuery(""); setNewTripCountryId(null);
    setNewTripStart(toISODate(today)); setNewTripEnd(toISODate(weekLater)); setShowNewTripForm(true);
  };

  const createTrip = () => {
    if (!newTripCountryId || !newTripName.trim()) return;
    const cty = allCountriesForMap.find((c) => c.id === newTripCountryId);
    if (!cty) return;
    const id = "trip_" + Date.now();
    const total = dayCount(newTripStart, newTripEnd);
    const trip = {
      id,
      name: newTripName.trim(),
      countryId: cty.id,
      countryName: cty.name,
      flag: cty.flag,
      startDate: newTripStart,
      endDate: newTripEnd,
      status: "planning",
      stops: [{ id: "stop_" + Date.now(), city: "", dayStart: 1, dayEnd: total, highlights: [], stays: [], meals: [] }],
      transits: [],
      dailyNotes: {},
      isPublic: false,
      shareId: null,
      createdAt: new Date().toISOString(),
    };
    saveTrips({ ...trips, [id]: trip });
    setShowNewTripForm(false);
    setActiveTripId(id);
    setView("trip-detail");
  };

  const deleteTrip = (tripId) => {
    const next = { ...trips };
    delete next[tripId];
    saveTrips(next);
    setActiveTripId(null);
    setView("trips");
  };

  // Single choke point for every trip mutation (stops, transits, stays, meals,
  // highlights, day activities, documents...). `updater` receives the current trip
  // and returns the next one; this keeps every edit path consistent and means a
  // Firestore write shape only needs to be correct in one place (saveTrips).
  const updateTrip = (tripId, updater) => {
    const current = trips[tripId];
    if (!current) return;
    saveTrips({ ...trips, [tripId]: updater(current) });
  };

  const reconcileTransits = (stops, transits) => {
    const byAfter = {};
    transits.forEach((tr) => { byAfter[tr.afterStopId] = tr; });
    const next = [];
    for (let i = 0; i < stops.length - 1; i++) {
      const key = stops[i].id;
      next.push(byAfter[key] || { afterStopId: key, mode: "", durationHours: "", durationMinutes: "", price: "" });
    }
    return next;
  };

  const makeBlankStop = (dayStart, dayEnd) => ({ id: "stop_" + Date.now() + "_" + Math.floor(Math.random() * 1000), city: "", dayStart, dayEnd, highlights: [], stays: [], meals: [] });

  const addStop = (tripId) => {
    updateTrip(tripId, (t) => {
      const lastStop = t.stops[t.stops.length - 1];
      const nextDay = lastStop ? lastStop.dayEnd + 1 : 1;
      const total = dayCount(t.startDate, t.endDate);
      const newStop = makeBlankStop(Math.min(nextDay, total), total);
      const stops = [...t.stops, newStop];
      return { ...t, stops, transits: reconcileTransits(stops, t.transits) };
    });
  };

  const insertStopBefore = (tripId, beforeStopId) => {
    updateTrip(tripId, (t) => {
      const idx = beforeStopId ? t.stops.findIndex((s) => s.id === beforeStopId) : 0;
      const refDay = idx >= 0 && t.stops[idx] ? t.stops[idx].dayStart : 1;
      const newStop = makeBlankStop(refDay, refDay);
      const stops = [...t.stops];
      stops.splice(idx < 0 ? 0 : idx, 0, newStop);
      return { ...t, stops, transits: reconcileTransits(stops, t.transits) };
    });
  };

  const removeStop = (tripId, stopId) => {
    updateTrip(tripId, (t) => {
      const stops = t.stops.filter((s) => s.id !== stopId);
      return { ...t, stops, transits: reconcileTransits(stops, t.transits) };
    });
  };

  const updateStopField = (tripId, stopId, field, value) => {
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, [field]: value } : s)),
    }));
  };

  const addHighlight = (tripId, stopId, text, source) => {
    if (!text.trim()) return;
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, highlights: [...s.highlights, { id: "h_" + Date.now(), text: text.trim(), source: source || "" }] } : s)),
    }));
  };

  const removeHighlight = (tripId, stopId, highlightId) => {
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, highlights: s.highlights.filter((h) => h.id !== highlightId) } : s)),
    }));
  };

  const updateTransit = (tripId, afterStopId, field, value) => {
    updateTrip(tripId, (t) => ({
      ...t,
      transits: t.transits.map((tr) => (tr.afterStopId === afterStopId ? { ...tr, [field]: value } : tr)),
    }));
  };

  const addStay = (tripId, stopId, name, nights, price) => {
    if (!name.trim()) return;
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, stays: [...s.stays, { id: "st_" + Date.now(), name: name.trim(), nights: nights || "", price: price || "" }] } : s)),
    }));
  };
  const removeStay = (tripId, stopId, stayId) => {
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, stays: s.stays.filter((st) => st.id !== stayId) } : s)),
    }));
  };
  const toggleStayConfirmed = (tripId, stopId, stayId) => {
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, stays: s.stays.map((st) => (st.id === stayId ? { ...st, confirmed: !st.confirmed } : st)) } : s)),
    }));
  };
  const toggleTransitConfirmed = (tripId, afterStopId) => {
    updateTrip(tripId, (t) => ({
      ...t,
      transits: t.transits.map((tr) => (tr.afterStopId === afterStopId ? { ...tr, confirmed: !tr.confirmed } : tr)),
    }));
  };
  const addDocument = (tripId, text) => {
    if (!text.trim()) return;
    updateTrip(tripId, (t) => ({ ...t, documents: [...(t.documents || []), { id: "doc_" + Date.now(), text: text.trim() }] }));
  };
  const removeDocument = (tripId, docId) => {
    updateTrip(tripId, (t) => ({ ...t, documents: (t.documents || []).filter((d) => d.id !== docId) }));
  };
  const addMeal = (tripId, stopId, name) => {
    if (!name.trim()) return;
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, meals: [...s.meals, { id: "ml_" + Date.now(), name: name.trim() }] } : s)),
    }));
  };
  const removeMeal = (tripId, stopId, mealId) => {
    updateTrip(tripId, (t) => ({
      ...t,
      stops: t.stops.map((s) => (s.id === stopId ? { ...s, meals: s.meals.filter((m) => m.id !== mealId) } : s)),
    }));
  };

  const addDayActivity = (tripId, dayNum, time, name) => {
    if (!name.trim()) return;
    updateTrip(tripId, (t) => {
      const days = { ...(t.days || {}) };
      const list = days[dayNum] || [];
      days[dayNum] = [...list, { id: "act_" + Date.now(), time: (time || "").trim(), name: name.trim() }];
      return { ...t, days };
    });
  };
  const removeDayActivity = (tripId, dayNum, activityId) => {
    updateTrip(tripId, (t) => {
      const days = { ...(t.days || {}) };
      days[dayNum] = (days[dayNum] || []).filter((a) => a.id !== activityId);
      return { ...t, days };
    });
  };
  const stopForDay = (trip, dayNum) => trip.stops.find((s) => dayNum >= s.dayStart && dayNum <= s.dayEnd) || trip.stops[0];

  const tripTotalCost = (trip) => {
    const transitSum = trip.transits.reduce((sum, tr) => sum + (parseFloat(tr.price) || 0), 0);
    const staySum = trip.stops.reduce((sum, s) => sum + (s.stays || []).reduce((ss, st) => ss + (parseFloat(st.price) || 0), 0), 0);
    return transitSum + staySum;
  };

  const TRANSIT_TYPICAL = {
    flight: "1-3h · €30-120",
    train: "4-15h · €10-50",
    bus: "5-18h · €5-30",
    car: lang === "pt" ? "varia com a distância" : "varies with distance",
    boat: "1-6h · €10-40",
  };

  // Builds the trip PDF page by page with jsPDF's low-level drawing API (no HTML
  // rendering available): 1) cover, 2) country summary (only if the heavy country
  // data has finished loading), 3) route timeline with day-by-day stops, 4) day
  // notes if any exist, 5) a closing page. Colors are plain RGB arrays because
  // jsPDF doesn't understand CSS custom properties — keep in sync with the
  // .wp-root palette by hand if the design tokens change.
  const exportTripPDF = (trip, countryData) => {
    if (!window.jspdf) return;
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();
    const margin = 18;
    const navy = [20, 32, 53];
    const gold = [184, 134, 62];
    const inkSoft = [131, 121, 95];
    const ink = [31, 27, 20];
    const hairline = [225, 214, 188];
    const parchment = [246, 242, 232];
    const accentRgb = (() => {
      const hex = (countryData && countryData.continentColor) || "#2F5D62";
      const n = parseInt(hex.slice(1), 16);
      return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
    })();

    const paintBg = () => { doc.setFillColor(parchment[0], parchment[1], parchment[2]); doc.rect(0, 0, pageWidth, pageHeight, "F"); };
    const compassMark = (cx, cy, r, ringColor, dotColor) => {
      doc.setDrawColor(ringColor[0], ringColor[1], ringColor[2]);
      doc.setLineWidth(0.6);
      doc.circle(cx, cy, r, "S");
      doc.setFillColor(dotColor[0], dotColor[1], dotColor[2]);
      doc.circle(cx, cy, r * 0.35, "F");
    };
    const brandStamp = (color) => {
      compassMark(margin + 3.2, margin + 3, 3.2, color, gold);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9);
      doc.setTextColor(color[0], color[1], color[2]);
      doc.text("WAYPOINT", margin + 9, margin + 4.5);
    };
    const footer = (pageColor) => {
      doc.setFontSize(7.5);
      doc.setTextColor(pageColor[0], pageColor[1], pageColor[2]);
      doc.text("hellowaypoint.com", pageWidth / 2, pageHeight - 9, { align: "center" });
    };

    // ---------- Page 1: cover ----------
    doc.setFillColor(navy[0], navy[1], navy[2]);
    doc.rect(0, 0, pageWidth, pageHeight, "F");
    doc.setFillColor(255, 255, 255);
    if (doc.GState && doc.setGState) {
      doc.setGState(new doc.GState({ opacity: 0.05 }));
      doc.circle(pageWidth - 25, 40, 55, "F");
      doc.setGState(new doc.GState({ opacity: 1 }));
    }
    brandStamp([246, 242, 232]);

    doc.setTextColor(246, 242, 232);
    doc.setFont("times", "bold");
    doc.setFontSize(13);
    doc.text((countryData ? countryData.name : (trip.countryName || "")).toUpperCase(), margin, pageHeight / 2 - 28);
    doc.setFontSize(34);
    const titleLines = doc.splitTextToSize(trip.name, pageWidth - margin * 2);
    let cy = pageHeight / 2 - 14;
    titleLines.forEach((line) => { doc.text(line, margin, cy); cy += 13; });

    doc.setDrawColor(184, 134, 62);
    doc.setLineWidth(0.6);
    doc.line(margin, cy + 2, margin + 30, cy + 2);

    doc.setFont("helvetica", "normal");
    doc.setFontSize(11);
    doc.setTextColor(220, 214, 196);
    doc.text((trip.startDate || "?") + "  –  " + (trip.endDate || "?"), margin, cy + 14);
    doc.setFontSize(9.5);
    doc.setTextColor(180, 190, 195);
    doc.text(dayCount(trip.startDate, trip.endDate) + " " + T.days + "  ·  " + trip.stops.length + " " + T.stops, margin, cy + 21);

    doc.setFont("times", "italic");
    doc.setFontSize(10);
    doc.setTextColor(190, 198, 200);
    doc.text(T.pdfCoverTagline, margin, pageHeight - 16);

    // ---------- Page 2: country summary (only if the full country data has loaded) ----------
    if (countryData && countryData.blurb) {
      doc.addPage();
      paintBg();
      brandStamp(navy);

      let y2 = margin + 22;
      doc.setFont("times", "bold");
      doc.setFontSize(20);
      doc.setTextColor(ink[0], ink[1], ink[2]);
      doc.text(countryData.name, margin, y2);
      y2 += 6;
      doc.setDrawColor(accentRgb[0], accentRgb[1], accentRgb[2]);
      doc.setLineWidth(0.8);
      doc.line(margin, y2, margin + 22, y2);
      y2 += 10;

      if (countryData.blurb) {
        doc.setFont("times", "italic");
        doc.setFontSize(11.5);
        doc.setTextColor(60, 55, 45);
        const blurbLines = doc.splitTextToSize(countryData.blurb, pageWidth - margin * 2);
        blurbLines.forEach((line) => { doc.text(line, margin, y2); y2 += 6.2; });
        y2 += 8;
      }

      const stats = [
        [T.pdfPopulation, countryData.population], [T.pdfLanguage, countryData.language],
        [T.pdfCurrency, countryData.currency], [T.pdfBestTime, countryData.bestTime],
      ].filter((s) => s[1]);
      if (stats.length > 0) {
        doc.setFont("helvetica", "bold");
        doc.setFontSize(8.5);
        doc.setTextColor(gold[0], gold[1], gold[2]);
        doc.text(T.pdfEssentialsTitle.toUpperCase(), margin, y2);
        y2 += 7;
        const colW = (pageWidth - margin * 2) / 2;
        stats.forEach((s, i) => {
          const cx = margin + (i % 2) * colW;
          const cyy = y2 + Math.floor(i / 2) * 16;
          doc.setFont("helvetica", "normal");
          doc.setFontSize(8);
          doc.setTextColor(inkSoft[0], inkSoft[1], inkSoft[2]);
          doc.text(String(s[0]).toUpperCase(), cx, cyy);
          doc.setFont("times", "normal");
          doc.setFontSize(11);
          doc.setTextColor(ink[0], ink[1], ink[2]);
          doc.text(String(s[1]), cx, cyy + 6);
        });
        y2 += Math.ceil(stats.length / 2) * 16 + 6;
      }

      if (countryData.budget) {
        doc.setFont("helvetica", "bold");
        doc.setFontSize(8.5);
        doc.setTextColor(gold[0], gold[1], gold[2]);
        doc.text(T.dailyBudget ? T.dailyBudget.toUpperCase() : "BUDGET", margin, y2);
        y2 += 6;
        doc.setFont("helvetica", "normal");
        doc.setFontSize(9.5);
        doc.setTextColor(60, 55, 45);
        const budgetLines = doc.splitTextToSize(countryData.budget, pageWidth - margin * 2);
        budgetLines.forEach((line) => { doc.text(line, margin, y2); y2 += 5.2; });
        y2 += 6;
      }
      if (countryData.visa) {
        doc.setFont("helvetica", "bold");
        doc.setFontSize(8.5);
        doc.setTextColor(gold[0], gold[1], gold[2]);
        doc.text(T.visa.toUpperCase(), margin, y2);
        y2 += 6;
        doc.setFont("helvetica", "normal");
        doc.setFontSize(9.5);
        doc.setTextColor(60, 55, 45);
        const visaLines = doc.splitTextToSize(countryData.visa, pageWidth - margin * 2);
        visaLines.forEach((line) => { doc.text(line, margin, y2); y2 += 5.2; });
      }
      footer(inkSoft);
    }

    // ---------- Page 3+: route timeline ----------
    doc.addPage();
    paintBg();
    brandStamp(navy);
    doc.setFont("times", "bold");
    doc.setFontSize(16);
    doc.setTextColor(ink[0], ink[1], ink[2]);
    doc.text(T.pdfRouteTitle, margin, margin + 20);

    let y = margin + 32;
    const dotX = margin + 3;
    const textX = margin + 12;
    const textWidth = pageWidth - textX - margin;

    trip.stops.forEach((stop, i) => {
      const dateRange = formatDayRange(trip, stop.dayStart, stop.dayEnd);
      const rawLines = [
        ...stop.highlights.map((h) => "· " + h.text),
        ...(stop.stays || []).map((st) => "🏨 " + st.name + (st.nights ? " (" + st.nights + " " + T.nights + ")" : "") + (st.price ? " · " + st.price : "")),
        ...(stop.meals || []).map((m) => "🍽 " + m.name),
      ];
      const allLines = rawLines.reduce((acc, line) => acc.concat(doc.splitTextToSize(line, textWidth)), []);
      const blockHeight = 16 + (dateRange ? 5 : 0) + allLines.length * 5.4 + 6;

      if (y + blockHeight > pageHeight - 20) { doc.addPage(); paintBg(); brandStamp(navy); y = margin + 20; }

      const dotTop = y;
      doc.setFillColor(i === 0 ? gold[0] : 255, i === 0 ? gold[1] : 255, i === 0 ? gold[2] : 255);
      doc.setDrawColor(gold[0], gold[1], gold[2]);
      doc.setLineWidth(0.5);
      doc.circle(dotX, dotTop, 2, i === 0 ? "F" : "FD");

      doc.setFont("times", "bold");
      doc.setFontSize(14);
      doc.setTextColor(ink[0], ink[1], ink[2]);
      doc.text(stop.city || T.cityPlaceholder, textX, y + 1.5);
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9);
      doc.setTextColor(inkSoft[0], inkSoft[1], inkSoft[2]);
      doc.text(T.day + " " + stop.dayStart + "-" + stop.dayEnd, pageWidth - margin, y + 1.5, { align: "right" });
      y += 6.5;
      if (dateRange) {
        doc.setFontSize(8);
        doc.setTextColor(inkSoft[0], inkSoft[1], inkSoft[2]);
        doc.text(dateRange, textX, y);
        y += 6;
      } else { y += 1; }

      doc.setFont("helvetica", "normal");
      doc.setFontSize(9.5);
      doc.setTextColor(60, 55, 45);
      allLines.forEach((line) => { doc.text(line, textX, y); y += 5.4; });

      const stopBottom = y + 3;

      const transit = trip.transits.find((tr) => tr.afterStopId === stop.id);
      const hasNext = i < trip.stops.length - 1;
      if (hasNext) {
        const lineBottom = transit && transit.mode ? stopBottom + 9 : stopBottom + 4;
        doc.setDrawColor(hairline[0], hairline[1], hairline[2]);
        doc.setLineWidth(0.4);
        doc.line(dotX, dotTop + 2, dotX, lineBottom);
        if (transit && transit.mode) {
          const durTxt = (transit.durationHours || transit.durationMinutes) ? " · " + (transit.durationHours || 0) + "h" + (transit.durationMinutes ? transit.durationMinutes + "m" : "") : "";
          doc.setFont("helvetica", "bold");
          doc.setFontSize(8);
          doc.setTextColor(gold[0], gold[1], gold[2]);
          doc.text((T["transit" + transit.mode.charAt(0).toUpperCase() + transit.mode.slice(1)] || transit.mode).toUpperCase() + durTxt + (transit.price ? " · " + transit.price : ""), textX, stopBottom + 5);
        }
        y = lineBottom + 6;
      } else {
        y = stopBottom + 4;
      }
    });

    if (y + 20 > pageHeight - 15) { doc.addPage(); paintBg(); brandStamp(navy); y = margin + 20; }
    y += 4;
    doc.setDrawColor(hairline[0], hairline[1], hairline[2]);
    doc.line(margin, y, pageWidth - margin, y);
    y += 9;
    doc.setFont("helvetica", "bold");
    doc.setFontSize(11);
    doc.setTextColor(ink[0], ink[1], ink[2]);
    doc.text(T.estimatedCost + ": EUR " + tripTotalCost(trip).toFixed(0), margin, y);
    footer(inkSoft);

    // ---------- Day notes (if any) ----------
    const noteDays = Array.from({ length: dayCount(trip.startDate, trip.endDate) }, (_, i) => i + 1)
      .filter((day) => ((trip.dailyNotes || {})[day] || "").trim());
    if (noteDays.length > 0) {
      doc.addPage();
      paintBg();
      brandStamp(navy);
      let ny = margin + 20;
      doc.setFont("times", "bold");
      doc.setFontSize(16);
      doc.setTextColor(ink[0], ink[1], ink[2]);
      doc.text(T.dayNotes, margin, ny);
      ny += 12;
      const maxTextWidth = pageWidth - margin * 2 - 4;
      noteDays.forEach((day) => {
        const text = String(trip.dailyNotes[day]).trim();
        const covering = trip.stops.find((s) => day >= s.dayStart && day <= s.dayEnd);
        const wrapped = doc.splitTextToSize(text, maxTextWidth);
        const blockH = 8 + wrapped.length * 5.4 + 4;
        if (ny + blockH > pageHeight - 20) { doc.addPage(); paintBg(); brandStamp(navy); ny = margin + 20; }
        doc.setFont("helvetica", "bold");
        doc.setFontSize(9.5);
        doc.setTextColor(gold[0], gold[1], gold[2]);
        doc.text(T.day + " " + day + (covering ? " · " + covering.city : ""), margin, ny);
        ny += 6;
        doc.setFont("times", "italic");
        doc.setFontSize(10);
        doc.setTextColor(60, 55, 45);
        wrapped.forEach((line) => { doc.text(line, margin, ny); ny += 5.4; });
        ny += 5;
      });
      footer(inkSoft);
    }

    // ---------- Final page: farewell ----------
    doc.addPage();
    doc.setFillColor(navy[0], navy[1], navy[2]);
    doc.rect(0, 0, pageWidth, pageHeight, "F");
    compassMark(pageWidth / 2, pageHeight / 2 - 26, 9, [246, 242, 232], gold);
    doc.setFont("times", "bold");
    doc.setFontSize(22);
    doc.setTextColor(246, 242, 232);
    doc.text(T.pdfFarewellTitle, pageWidth / 2, pageHeight / 2 - 2, { align: "center" });
    doc.setFont("times", "italic");
    doc.setFontSize(11.5);
    doc.setTextColor(210, 216, 210);
    const farewellLines = doc.splitTextToSize(T.pdfFarewellLine, pageWidth - margin * 4);
    let fy = pageHeight / 2 + 10;
    farewellLines.forEach((line) => { doc.text(line, pageWidth / 2, fy, { align: "center" }); fy += 6.5; });
    doc.setFont("helvetica", "normal");
    doc.setFontSize(9.5);
    doc.setTextColor(gold[0], gold[1], gold[2]);
    doc.text(T.pdfFarewellSign, pageWidth / 2, fy + 8, { align: "center" });

    doc.save(trip.name.replace(/[^a-z0-9]/gi, "_") + ".pdf");
  };

  const markTripDone = (tripId) => {
    updateTrip(tripId, (t) => ({ ...t, status: "done" }));
    const trip = trips[tripId];
    if (trip) setCountryStatus(trip.countryId, "visited");
  };

  return (
    <div className="wp-root">
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700&display=swap');
        .wp-root {
          --parchment: #F6F8FC; --parchment-deep: #E9EEF5; --ink: #14213D; --ink-soft: #586579; --hairline: #E3E8EF;
          --navy: #2457E6; --navy-hover: #1843BF; --navy-subtle: #EDF3FF; --gold: #FF8A3D; --gold-subtle: #FFF2E8;
          --success: #1E8E5A; --danger: #D64545;
          font-family: 'Work Sans', sans-serif; background: var(--parchment); color: var(--ink);
          min-height: 100vh; width: 100%; box-sizing: border-box;
          padding: calc(env(safe-area-inset-top, 0px) + 1.75rem) 1.25rem 4rem;
        }
        html, body { overflow-x: hidden; max-width: 100%; }
        .wp-root * { box-sizing: border-box; }
        @media (prefers-reduced-motion: reduce) {
          .wp-root *, .wp-root *::before, .wp-root *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
            scroll-behavior: auto !important;
          }
        }
        .wp-shell { max-width: 780px; margin: 0 auto; }

        .wp-hero { display: flex; align-items: center; gap: 1.5rem; margin-bottom: 2rem; flex-wrap: wrap; }
        .wp-hero-text { flex: 1; min-width: 220px; }
        .wp-hero-visual { flex: 0 0 260px; max-width: 100%; }
        .wp-hero-svg { width: 100%; height: auto; display: block; }
        @media (max-width: 599px) {
          .wp-hero-visual { display: none; }
        }
        .wp-brand { display: flex; align-items: center; gap: 0.55rem; margin-bottom: 0.4rem; }
        .wp-brand-mark { width: 30px; height: 30px; border-radius: 50%; background: var(--navy); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
        .wp-title { font-size: 2rem; font-weight: 600; letter-spacing: -0.01em; margin: 0; }
        .wp-hero-headline { font-size: 2.6rem; font-weight: 600; letter-spacing: -0.02em; line-height: 1.04; margin: 0 0 0.9rem; }
        @media (min-width: 600px) { .wp-hero-headline { font-size: 3.1rem; } }
        .wp-tagline { font-size: 0.96rem; color: var(--ink-soft); margin: 0 0 1.1rem; max-width: 54ch; line-height: 1.5; }
        .wp-hero-stats { display: flex; gap: 1.7rem; margin-bottom: 1.4rem; }
        .wp-hero-stat { display: flex; flex-direction: column; min-width: 5.4rem; }
        .wp-hero-stat b { font-size: 1.4rem; font-weight: 600; display: block; line-height: 1.2; }
        .wp-hero-stat span { font-size: 0.76rem; color: var(--ink-soft); }
        .wp-hero-features { display: flex; flex-direction: column; gap: 0.6rem; max-width: 30rem; margin-bottom: 1.8rem; }
        .wp-hero-feature-card { display: flex; align-items: flex-start; gap: 0.7rem; text-align: left; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.7rem 0.9rem; cursor: pointer; color: var(--ink); }
        .wp-hero-feature-card:hover { border-color: var(--gold); }
        .wp-hero-feature-card svg { flex-shrink: 0; margin-top: 0.15rem; color: var(--gold); }
        .wp-hero-feature-card b { display: block; font-size: 0.95rem; font-weight: 600; margin-bottom: 0.1rem; }
        .wp-hero-feature-card span { display: block; font-size: 0.8rem; color: var(--ink-soft); line-height: 1.35; }
        @media (min-width: 640px) { .wp-hero-features { flex-direction: row; } .wp-hero-feature-card { flex: 1; } }

        .wp-back { display: inline-flex; align-items: center; gap: 0.4rem; background: none; border: none; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.88rem; color: var(--ink-soft); padding: 0.3rem 0; margin-bottom: 1.1rem; }
        .wp-back:hover { color: var(--ink); }

        .wp-continent-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.85rem; margin-bottom: 0.5rem; }
        @media (min-width: 560px) {
          .wp-continent-grid {
            grid-template-columns: repeat(3, 1fr);
            grid-template-areas: "europe europe asia" "africa namerica samerica" "oceania oceania oceania";
          }
          .wp-cont-europe { grid-area: europe; }
          .wp-cont-asia { grid-area: asia; }
          .wp-cont-africa { grid-area: africa; }
          .wp-cont-north-america { grid-area: namerica; }
          .wp-cont-south-america { grid-area: samerica; }
          .wp-cont-oceania { grid-area: oceania; }
        }
        .wp-continent-tile {
          background: color-mix(in srgb, var(--tile-color) 9%, #fff);
          border: 1px solid color-mix(in srgb, var(--tile-color) 28%, var(--hairline));
          border-radius: 12px; padding: 1.2rem 1.3rem; text-align: left; cursor: pointer; font-family: inherit;
          display: flex; flex-direction: column; justify-content: space-between; gap: 0.7rem;
          min-height: 148px; transition: transform 0.16s ease, box-shadow 0.16s ease;
        }
        .wp-continent-tile:hover { transform: translateY(-3px); box-shadow: 0 10px 22px rgba(31,27,20,0.1); }
        .wp-continent-icon { color: var(--tile-color); opacity: 0.9; }
        .wp-continent-name { font-size: 1.25rem; font-weight: 600; }
        .wp-continent-tagline { font-size: 0.82rem; color: var(--ink-soft); line-height: 1.35; margin-top: 0.2rem; }
        .wp-continent-count { font-size: 0.95rem; color: var(--tile-color); }
        .wp-continent-count b { font-size: 1.5rem; font-weight: 700; margin-right: 0.3rem; }
        .wp-tile-big { grid-column: span 2; }
        .wp-tile-big .wp-continent-name { font-size: 1.55rem; }
        .wp-tile-wide { grid-column: span 2; }
        @media (min-width: 560px) { .wp-tile-wide { grid-column: span 3; flex-direction: row; align-items: center; min-height: auto; padding: 1.3rem 1.6rem; } }
        .wp-tile-wide .wp-continent-body { flex: 1; }

        .wp-quiz-section { margin-bottom: 1.8rem; }
        .wp-quiz-card { background: #fff; border: 1px solid var(--hairline); border-radius: 10px; padding: 1.5rem 1.4rem; }
        .wp-quiz-intro { text-align: center; display: flex; flex-direction: column; align-items: center; background: var(--navy); border: none; color: #EFE9DA; position: relative; overflow: hidden; padding: 2.2rem 1.8rem; }
        .wp-quiz-intro::before { content: ""; position: absolute; top: -35%; right: -12%; width: 240px; height: 240px; border-radius: 50%; background: radial-gradient(circle, rgba(184,134,62,0.4), transparent 70%); pointer-events: none; }
        .wp-quiz-intro > * { position: relative; }
        .wp-quiz-intro .wp-section-title { color: #fff; }
        .wp-quiz-intro .wp-now-subtitle { color: #B7BECC; }
        .wp-quiz-intro .wp-quiz-btn-primary { background: var(--gold); color: var(--navy); border-color: var(--gold); }
        .wp-quiz-intro .wp-quiz-btn:not(.wp-quiz-btn-primary) { background: transparent; border-color: rgba(239,233,218,0.4); color: #EFE9DA; }
        .wp-quiz-progress { font-size: 0.8rem; color: var(--ink-soft); font-weight: 600; margin-bottom: 0.9rem; }
        .wp-quiz-clue-wrap { min-height: 70px; display: flex; align-items: center; justify-content: center; margin-bottom: 0.8rem; }
        .wp-quiz-flag-big { font-size: 3.5rem; line-height: 1; }
        .wp-quiz-clue-text { font-size: 1.25rem; text-align: center; line-height: 1.4; color: var(--ink); }
        .wp-quiz-clue-food { font-size: 1.05rem; text-align: center; line-height: 1.5; }
        .wp-quiz-prompt { text-align: center; font-size: 0.9rem; color: var(--ink-soft); margin: 0 0 1.1rem; }
        .wp-quiz-options { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.6rem; }
        @media (max-width: 480px) { .wp-quiz-options { grid-template-columns: 1fr; } }
        .wp-quiz-option { background: var(--parchment); border: 1px solid var(--hairline); border-radius: 3px; padding: 0.7rem 0.9rem; font-family: inherit; font-size: 0.92rem; cursor: pointer; text-align: left; display: flex; align-items: center; gap: 0.5rem; }
        .wp-quiz-option:hover:not(:disabled) { border-color: var(--navy); }
        .wp-quiz-option:disabled { cursor: default; }
        .wp-quiz-option-correct { background: #E4EFE2; border-color: #6B9E68; font-weight: 600; }
        .wp-quiz-option-wrong { background: #F5E2E0; border-color: #C1665F; }
        .wp-quiz-btn { background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.65rem 1.4rem; font-family: 'Work Sans', sans-serif; font-size: 0.9rem; font-weight: 600; cursor: pointer; color: var(--ink); display: inline-flex; align-items: center; gap: 0.4rem; }
        .wp-quiz-btn-primary { background: var(--navy); color: #F3EDE0; border-color: var(--navy); }
        .wp-quiz-score { font-size: 2.6rem; font-weight: 600; margin: 0.5rem 0 0.15rem; color: #fff; }
        .wp-quiz-rank { font-size: 1rem; color: #B7BECC; margin-bottom: 1.2rem; }
        .wp-quiz-actions { display: flex; gap: 0.7rem; flex-wrap: wrap; justify-content: center; }

        .wp-monthly-wrap { border-top: 1px solid var(--hairline); padding-top: 2.4rem; margin-top: 0.5rem; margin-bottom: 1.8rem; }
        .wp-monthly-eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: var(--gold); font-weight: 600; margin-bottom: 1.2rem; }
        .wp-monthly-eyebrow .wp-monthly-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--gold); }
        .wp-now-section + .wp-quiz-section { border-top: 1px solid var(--hairline); padding-top: 1.6rem; margin-top: 0.4rem; }

        .wp-now-section { margin-bottom: 1.8rem; }
        .wp-now-subtitle { font-size: 0.86rem; color: var(--ink-soft); margin: 0 0 1rem; }
        .wp-now-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.9rem; }
        .wp-now-card { text-align: left; cursor: pointer; font-family: inherit; background: none; border: none; padding: 0; display: flex; flex-direction: column; gap: 0.35rem; }
        .wp-now-flag { font-size: 1.5rem; line-height: 1; }
        .wp-now-name { font-size: 1.1rem; font-weight: 600; border-bottom: 2px solid transparent; display: inline-block; width: fit-content; transition: border-color 0.15s ease; }
        .wp-now-card:hover .wp-now-name { border-bottom-color: var(--gold); }
        .wp-now-reason { font-size: 0.85rem; color: #4a4436; line-height: 1.5; }

        .wp-search-wrap { margin-bottom: 1.3rem; }
        .wp-search-box { display: flex; align-items: center; gap: 0.65rem; background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.85rem 1.3rem; box-shadow: 0 1px 2px rgba(31,27,20,0.04); }
        .wp-search-icon { color: var(--ink-soft); flex-shrink: 0; }
        .wp-search-input { flex: 1; min-width: 0; border: none; outline: none; background: transparent; font-family: 'Work Sans', sans-serif; font-size: 0.95rem; color: var(--ink); }
        .wp-search-input::placeholder { color: var(--ink-soft); }
        .wp-search-clear { background: none; border: none; cursor: pointer; color: var(--ink-soft); padding: 0.15rem; display: flex; align-items: center; flex-shrink: 0; }
        .wp-search-clear:hover { color: var(--ink); }
        .wp-search-empty { font-size: 0.92rem; color: var(--ink-soft); padding: 0.6rem 0 1rem; }

        .wp-country-row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; width: 100%; background: #fff; border: 1px solid var(--hairline); border-left: 4px solid var(--row-color); border-radius: 2px; padding: 0.95rem 1.1rem; cursor: pointer; text-align: left; font-family: inherit; margin-bottom: 0.6rem; }
        .wp-country-row:hover { background: #FBF8F1; }
        .wp-country-name { font-size: 1.08rem; font-weight: 500; display: flex; align-items: center; gap: 0.5rem; }
        .wp-country-capital { font-size: 0.82rem; color: var(--ink-soft); margin-top: 0.15rem; }

        .wp-detail-hero { margin-bottom: 1.6rem; }
        .wp-detail-name { font-size: 2.1rem; font-weight: 600; margin: 0 0 0.2rem; letter-spacing: -0.01em; display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap; }
        .wp-detail-sub { font-size: 0.92rem; color: var(--ink-soft); }

        .wp-stat-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.1rem; background: #fff; border: 1px solid var(--hairline); border-radius: 3px; padding: 1.1rem 1.2rem; margin-bottom: 1.6rem; }
        @media (min-width: 520px) { .wp-stat-grid { grid-template-columns: repeat(4, 1fr); } }

        .wp-section-title { font-size: 1.25rem; font-weight: 500; margin: 0 0 0.9rem; }
        .wp-blurb { font-size: 0.98rem; line-height: 1.6; margin-bottom: 1.9rem; max-width: 62ch; }

        .wp-attractions-grid { display: grid; grid-template-columns: 1fr; gap: 1.8rem; margin-bottom: 1.9rem; }
        @media (min-width: 620px) { .wp-attractions-grid { grid-template-columns: 1fr 1fr; } }
        .wp-attraction-img { width: 100%; height: 180px; object-fit: cover; border-radius: 8px; background: #EDE6D4; margin-bottom: 0.8rem; display: block; }
        .wp-attraction-img-loading { background: linear-gradient(90deg, #EDE6D4 25%, #F5F0E3 37%, #EDE6D4 63%); background-size: 400% 100%; animation: wp-shimmer 1.4s ease infinite; }
        @keyframes wp-shimmer { 0% { background-position: 100% 50%; } 100% { background-position: 0 50%; } }
        .wp-attraction-img-empty { display: flex; align-items: center; justify-content: center; }
        .wp-attraction-name { font-weight: 600; font-size: 1.05rem; margin-bottom: 0.35rem; }
        .wp-attraction-desc { font-size: 0.88rem; color: #4a4436; line-height: 1.55; }
        .wp-read-more-btn { background: none; border: none; padding: 0.3rem 0; margin-top: 0.2rem; font-size: 0.82rem; font-weight: 600; color: var(--navy); cursor: pointer; }
        .wp-read-more-btn:hover { text-decoration: underline; }
        .wp-map-toggle-btn { display: inline-flex; align-items: center; gap: 0.5rem; background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.6rem 1.1rem; font-size: 0.85rem; font-weight: 600; color: var(--navy); cursor: pointer; margin-bottom: 1rem; }
        .wp-map-toggle-btn:hover { background: var(--navy-subtle); }

        .wp-itinerary-wrap { margin-top: 1.9rem; margin-bottom: 0.5rem; }
        .wp-itinerary-head { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; margin-bottom: 1rem; }
        .wp-itinerary-total { font-size: 0.85rem; color: var(--ink-soft); white-space: nowrap; }

        .wp-route { position: relative; padding-left: 2.4rem; margin-top: 1.6rem; }
        .wp-route::before { content: ""; position: absolute; left: 9px; top: 6px; bottom: 26px; width: 1.5px; background-image: linear-gradient(var(--gold), var(--gold)); background-size: 2px 9px; background-repeat: repeat-y; opacity: 0.6; }
        .wp-day { position: relative; padding: 0 0 1.9rem; }
        .wp-day::before { content: ""; position: absolute; left: -2.4rem; top: 3px; width: 11px; height: 11px; border-radius: 50%; background: var(--accent-color); border: 3px solid var(--parchment); box-shadow: 0 0 0 1.5px var(--gold); }
        .wp-day:last-child::before { background: var(--gold); }
        .wp-day:last-child { padding-bottom: 0; }
        .wp-day-label { font-size: 0.8rem; color: var(--gold); font-weight: 600; margin-bottom: 0.2rem; display: block; }
        .wp-day-title { font-weight: 600; font-size: 1.12rem; margin-bottom: 0.3rem; }
        .wp-day-desc { font-size: 0.9rem; color: #4a4436; line-height: 1.5; }

        .wp-nav { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 0 0 1.3rem; border-bottom: 1px solid var(--hairline); margin-bottom: 1.6rem; }
        .wp-nav-brand { display: flex; align-items: center; gap: 0.5rem; background: none; border: none; cursor: pointer; font-size: 1.05rem; font-weight: 600; color: var(--ink); padding: 0; }
        .wp-nav-links { display: none; }
        .wp-hamburger-btn { display: flex; background: none; border: none; cursor: pointer; color: var(--ink); padding: 0.4rem; margin: -0.4rem; border-radius: 8px; }
        .wp-hamburger-btn:hover { background: var(--parchment-deep); }
        .wp-nav-account-badge { display: flex; align-items: center; justify-content: center; width: 30px; height: 30px; border-radius: 50%; border: none; cursor: pointer; font-size: 0.8rem; font-weight: 700; flex-shrink: 0; }
        .wp-nav-account-badge-in { background: var(--navy); color: #fff; }
        .wp-nav-account-badge-out { background: var(--parchment-deep); color: var(--ink-soft); border: 1px solid var(--hairline); }
        .wp-nav-account-badge-out:hover { background: var(--navy-subtle); color: var(--navy); }
        .wp-mobile-menu-overlay { position: fixed; inset: 0; background: rgba(20,33,61,0.4); z-index: 1000; display: flex; justify-content: flex-end; }
        .wp-mobile-menu-panel { width: 100%; max-width: 360px; height: 100%; background: #fff; display: flex; flex-direction: column; box-shadow: -8px 0 24px rgba(20,33,61,0.15); padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
        .wp-mobile-menu-head { display: flex; align-items: center; justify-content: space-between; padding: 1.1rem 1.25rem; border-bottom: 1px solid var(--hairline); flex-shrink: 0; }
        .wp-mobile-menu-close { background: none; border: none; cursor: pointer; color: var(--ink-soft); padding: 0.4rem; border-radius: 8px; }
        .wp-mobile-menu-close:hover { background: var(--parchment-deep); color: var(--ink); }
        .wp-mobile-menu-scroll { flex: 1; overflow-y: auto; padding: 1rem 0.75rem 1.5rem; }
        .wp-mobile-menu-label { margin: 0.4rem 1rem 0.5rem; font-size: 0.7rem; letter-spacing: 0.05em; color: var(--ink-soft); font-weight: 600; }
        .wp-mobile-menu-item { display: flex; align-items: center; gap: 0.9rem; width: 100%; background: none; border: none; cursor: pointer; text-align: left; padding: 0.85rem 1rem; border-radius: 10px; font-family: 'Work Sans', sans-serif; font-size: 0.98rem; color: var(--ink); min-height: 44px; }
        .wp-mobile-menu-item:hover { background: var(--parchment-deep); }
        .wp-mobile-menu-item-active { background: var(--navy-subtle); color: var(--navy); font-weight: 600; }
        .wp-mobile-menu-item-active svg { color: var(--navy); }
        .wp-mobile-menu-sep { height: 1px; background: var(--hairline); margin: 0.7rem 0.75rem; }
        .wp-mobile-menu-lang-row { display: flex; align-items: center; justify-content: space-between; padding: 0.85rem 1rem; }
        .wp-mobile-menu-lang-label { font-size: 0.85rem; color: var(--ink-soft); }

        .wp-task-sheet-overlay { position: fixed; inset: 0; background: rgba(20,33,61,0.4); z-index: 1100; display: flex; align-items: flex-end; justify-content: center; }
        .wp-task-sheet-panel { width: 100%; max-height: 88vh; background: #fff; border-radius: 16px 16px 0 0; display: flex; flex-direction: column; box-shadow: 0 -8px 24px rgba(20,33,61,0.15); padding-bottom: env(safe-area-inset-bottom, 0px); }
        @media (min-width: 640px) {
          .wp-task-sheet-overlay { align-items: center; }
          .wp-task-sheet-panel { width: 100%; max-width: 460px; max-height: 80vh; border-radius: 16px; }
        }
        .wp-task-sheet-head { display: flex; align-items: flex-start; justify-content: space-between; padding: 1.2rem 1.3rem 0.9rem; border-bottom: 1px solid var(--hairline); flex-shrink: 0; }
        .wp-task-sheet-title { margin: 0; font-size: 1.05rem; font-weight: 600; color: var(--ink); }
        .wp-task-sheet-context { margin: 0.15rem 0 0; font-size: 0.82rem; color: var(--ink-soft); }
        .wp-task-sheet-scroll { flex: 1; overflow-y: auto; padding: 1.2rem 1.3rem; }
        .wp-task-sheet-footer { padding: 0.9rem 1.3rem; border-top: 1px solid var(--hairline); flex-shrink: 0; }
        .wp-trip-transit-edit-form { display: flex; flex-direction: column; gap: 1rem; }
        .wp-trip-field-group { display: flex; flex-direction: column; gap: 0.35rem; }
        .wp-trip-field-label { font-size: 0.72rem; font-weight: 600; color: var(--ink-soft); text-transform: uppercase; letter-spacing: 0.02em; }
        .wp-trip-transit-duration-row { display: flex; gap: 0.6rem; }
        .wp-nav-link { background: none; border: none; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.88rem; color: var(--ink-soft); padding: 0.3rem 0; border-bottom: 2px solid transparent; }
        .wp-nav-link:hover { color: var(--ink); }
        .wp-nav-link-active { color: var(--ink); border-bottom-color: var(--navy); font-weight: 600; }
        .wp-lang-toggle { display: flex; align-items: center; gap: 0.3rem; padding-left: 1rem; border-left: 1px solid var(--hairline); }
        .wp-lang-btn { background: none; border: none; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.82rem; color: var(--ink-soft); padding: 0.2rem 0.15rem; }
        .wp-lang-btn:hover { color: var(--ink); }
        .wp-lang-btn-active { color: var(--ink); font-weight: 700; }
        .wp-lang-sep { color: var(--hairline); font-size: 0.8rem; }

        .wp-signin-btn { background: var(--navy); color: #fff; border: none; border-radius: 11px; padding: 0.45rem 1rem; font-family: 'Work Sans', sans-serif; font-size: 0.85rem; font-weight: 600; cursor: pointer; }
        .wp-user-menu-wrap { position: relative; }
        .wp-user-chip { display: inline-flex; align-items: center; gap: 0.4rem; background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.4rem 0.85rem; font-family: 'Work Sans', sans-serif; font-size: 0.82rem; color: var(--ink); cursor: pointer; }
        .wp-user-dropdown { position: absolute; right: 0; top: calc(100% + 0.4rem); background: #fff; border: 1px solid var(--hairline); border-radius: 8px; box-shadow: 0 8px 20px rgba(31,27,20,0.12); padding: 0.4rem; min-width: 140px; z-index: 30; }
        .wp-user-dropdown-item { display: flex; align-items: center; gap: 0.5rem; width: 100%; background: none; border: none; text-align: left; padding: 0.5rem 0.6rem; border-radius: 5px; font-family: 'Work Sans', sans-serif; font-size: 0.85rem; color: var(--ink); cursor: pointer; }
        .wp-user-dropdown-item:hover { background: var(--parchment); }

        .wp-status-row { display: flex; gap: 0.6rem; margin-top: 0.9rem; }
        .wp-status-btn { display: inline-flex; align-items: center; gap: 0.4rem; background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.4rem 0.9rem; font-family: 'Work Sans', sans-serif; font-size: 0.82rem; font-weight: 600; color: var(--ink-soft); cursor: pointer; }
        .wp-status-btn:hover { border-color: var(--ink-soft); }
        .wp-status-visited.wp-status-active { background: #E4EFE9; border-color: #3F8F6F; color: #2E6B52; }
        .wp-status-want.wp-status-active { background: #E3EEF5; border-color: #3E7CB1; color: #2A5A80; }

        .wp-status-dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-left: 0.5rem; vertical-align: middle; }
        .wp-status-dot-visited { background: #3F8F6F; }
        .wp-status-dot-want { background: #3E7CB1; }
        .wp-status-dot-none { background: #FFFFFF; border: 1px solid var(--hairline); box-sizing: border-box; }

        .wp-map-signin-banner { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; background: #fff; border: 1px solid var(--hairline); border-radius: 10px; padding: 0.9rem 1.2rem; margin-bottom: 1.2rem; font-size: 0.9rem; color: var(--ink-soft); }
        .wp-map-legend { display: flex; gap: 1.4rem; flex-wrap: wrap; margin-bottom: 1rem; font-size: 0.85rem; color: var(--ink-soft); }
        .wp-map-legend-item { display: inline-flex; align-items: center; }
        .wp-map-legend-item .wp-status-dot { margin-left: 0; margin-right: 0.45rem; }
        .wp-map-frame { position: relative; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.8rem; overflow: hidden; }
        .wp-world-map { width: 100%; height: auto; display: block; transform-origin: center center; }
        .wp-leaflet-frame { padding: 0; height: 520px; }
        .wp-map-loading { position: absolute; inset: 0; z-index: 600; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.6rem; background: var(--parchment); border-radius: 11px; font-size: 0.85rem; color: var(--ink-soft); }
        .wp-map-loading-spinner { width: 22px; height: 22px; border: 2.5px solid var(--hairline); border-top-color: var(--gold); border-radius: 50%; animation: wp-spin 0.8s linear infinite; }
        @keyframes wp-spin { to { transform: rotate(360deg); } }
        .wp-detail-loading { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.7rem; padding: 3rem 1rem; color: var(--ink-soft); font-size: 0.9rem; }
        .wp-leaflet-map { width: 100%; height: 100%; border-radius: 11px; background: #DCE8EE; }
        .wp-map-reset-btn { position: absolute; right: 0.7rem; bottom: 0.7rem; z-index: 500; width: 34px; height: 34px; border-radius: 8px; background: #fff; border: 2px solid rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--ink); }
        .wp-map-reset-btn:hover { background: var(--parchment); }
        @media (max-width: 640px) { .wp-leaflet-frame { height: 400px; } }
        .wp-map-country { stroke: var(--hairline); stroke-width: 1; cursor: pointer; transition: opacity 0.12s ease, fill 0.12s ease, filter 0.12s ease; }
        .wp-map-country:hover { filter: brightness(1.08); }
        .wp-map-status-none { fill: #FFFFFF; }
        .wp-map-status-visited { fill: #3F8F6F; }
        .wp-map-status-want { fill: #3E7CB1; }
        .wp-map-marker { stroke: var(--hairline); stroke-width: 1.5; }
        .wp-map-status-none:hover { fill: #E9EEF5; }
        .wp-map-bg-country { fill: #FFFFFF; stroke: var(--hairline); stroke-width: 1; pointer-events: none; }
        .wp-map-bg-country.wp-map-clickable { pointer-events: auto; cursor: pointer; }
        .wp-map-bg-country.wp-map-clickable:hover { fill: #E9EEF5; }
        .wp-map-marker.wp-map-clickable { cursor: pointer; }

        .wp-map-progress-row { display: flex; align-items: center; gap: 1.2rem; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 1.2rem; }
        .wp-map-progress-stat { flex-shrink: 0; }
        .wp-map-progress-value { font-size: 1.8rem; margin: 0; color: var(--ink); line-height: 1; }
        .wp-map-progress-label { font-size: 0.75rem; color: var(--ink-soft); margin: 0.2rem 0 0; }
        .wp-map-sparkline { flex: 1; height: 46px; min-width: 0; }

        .wp-map-zoom-controls { position: absolute; right: 1rem; bottom: 1rem; display: flex; flex-direction: column; gap: 0.3rem; }
        .wp-map-zoom-controls button { width: 32px; height: 32px; border-radius: 8px; background: #fff; border: 1px solid var(--hairline); color: var(--ink); cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
        .wp-map-zoom-controls button:hover { border-color: var(--gold); }
        .wp-map-zoom-reset { margin-top: 0.2rem; }

        .wp-map-popover { background: #fff; border-radius: 14px; padding: 1.3rem 1.4rem; max-width: 320px; width: 90%; position: relative; }
        .wp-map-popover-name { font-size: 1.15rem; margin: 0; display: flex; align-items: center; gap: 0.5rem; }
        .wp-map-popover-cont { font-size: 0.82rem; color: var(--ink-soft); margin: 0.2rem 0 0; }

        .wp-map-search-results { background: #fff; border: 1px solid var(--hairline); border-top: none; border-radius: 0 0 10px 10px; margin-bottom: 1.4rem; overflow: hidden; }
        .wp-map-search-row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; padding: 0.8rem 1rem; border-top: 1px solid var(--hairline); }
        .wp-map-search-row:first-child { border-top: none; }
        .wp-map-search-row-info { cursor: pointer; flex: 1; min-width: 180px; }
        .wp-map-search-row-info:hover .wp-country-name { text-decoration: underline; }

        .wp-map-lists { display: grid; grid-template-columns: 1fr; gap: 1.6rem; margin-top: 1.6rem; }
        @media (min-width: 700px) { .wp-map-lists { grid-template-columns: 1fr 1fr; } }
        .wp-map-list-title { font-size: 1.2rem; margin: 0 0 0.8rem; display: flex; align-items: center; gap: 0.5rem; }
        .wp-map-list-count { font-family: 'Work Sans', sans-serif; font-size: 0.8rem; font-weight: 600; color: var(--ink-soft); background: var(--parchment); border-radius: 999px; padding: 0.1rem 0.6rem; }
        .wp-map-list-empty { color: var(--ink-soft); font-size: 0.9rem; }
        .wp-map-list-group { margin-bottom: 1rem; }
        .wp-map-list-continent { font-size: 0.75rem; font-weight: 600; text-transform: none; color: var(--ink-soft); margin-bottom: 0.3rem; }
        .wp-map-list-row { display: flex; align-items: center; gap: 0.5rem; width: 100%; text-align: left; background: none; border: none; padding: 0.35rem 0; font-family: 'Work Sans', sans-serif; font-size: 0.92rem; color: var(--ink); cursor: pointer; }

        .wp-trips-page { max-width: 640px; }
        .wp-trip-card { display: block; width: 100%; text-align: left; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.9rem 1.1rem; margin-bottom: 0.7rem; cursor: pointer; }

        /* ---- Trip planner redesign ---- */
        .wp-trips-stat-strip { display: flex; gap: 1px; background: var(--hairline); border: 1px solid var(--hairline); border-radius: 12px; overflow: hidden; margin-bottom: 1.4rem; }
        .wp-trips-stat-cell { flex: 1; background: #fff; padding: 0.85rem 1.2rem; min-width: 120px; }
        .wp-trips-stat-label { margin: 0 0 0.2rem; font-size: 0.68rem; color: var(--ink-soft); font-weight: 500; letter-spacing: 0.02em; }
        .wp-trips-stat-value { margin: 0; font-size: 1.35rem; }
        .wp-trips-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.1rem; }
        .wp-trip-card-v2 { display: block; text-align: left; background: #fff; border: 1px solid var(--hairline); border-radius: 14px; overflow: hidden; cursor: pointer; box-shadow: 0 1px 2px rgba(20,32,53,0.04), 0 6px 18px rgba(20,32,53,0.05); }
        .wp-trip-card-v2-photo { height: 128px; position: relative; }
        .wp-trip-card-v2-flag { position: absolute; top: 0.7rem; right: 0.8rem; font-size: 1.4rem; }
        .wp-trip-card-v2-icon { position: absolute; bottom: 0.6rem; left: 0.8rem; width: 30px; height: 30px; border-radius: 8px; background: rgba(20,32,53,0.35); display: flex; align-items: center; justify-content: center; color: var(--parchment); }
        .wp-trip-card-v2-body { padding: 1rem 1.1rem 1.15rem; }
        .wp-trip-card-v2-name { margin: 0 0 0.2rem; font-size: 1.1rem; font-weight: 600; }
        .wp-trip-card-v2-meta { margin: 0 0 0.7rem; font-size: 0.78rem; color: var(--ink-soft); }
        .wp-trip-card-v2-badge { display: inline-block; font-size: 0.68rem; font-weight: 600; padding: 0.25rem 0.6rem; border-radius: 6px; background: var(--navy); color: var(--parchment); }
        .wp-trip-card-v2-badge-done { background: #3F8F6F; color: #fff; }

        .wp-trip-hero { margin: -1.5rem -1.2rem 2rem; padding: 2.2rem 1.4rem 1.8rem; background: linear-gradient(120deg, var(--navy), var(--trip-accent, #2F5D62) 75%); border-radius: 0 0 20px 20px; position: relative; overflow: hidden; color: var(--parchment); }
        .wp-trip-hero-icon-bg { position: absolute; right: -30px; top: -30px; opacity: 0.14; }
        .wp-trip-hero-back { display: inline-flex; align-items: center; gap: 0.35rem; text-decoration: none; color: rgba(246,242,232,0.75); font-size: 0.82rem; margin-bottom: 0.9rem; background: none; border: none; cursor: pointer; padding: 0; }
        .wp-trip-hero-row { display: flex; align-items: flex-end; justify-content: space-between; gap: 1rem; flex-wrap: wrap; position: relative; z-index: 1; }
        .wp-trip-hero-title { display: flex; align-items: center; gap: 0.6rem; }
        .wp-trip-hero-flag { font-size: 1.7rem; }
        .wp-trip-hero-name { margin: 0; font-weight: 600; font-size: 1.7rem; color: var(--parchment); }
        .wp-trip-hero-meta { margin: 0.5rem 0 0 2.35rem; font-size: 0.85rem; color: rgba(246,242,232,0.8); }
        .wp-trip-hero-cost { text-align: right; }
        .wp-trip-hero-cost-label { margin: 0; font-size: 0.7rem; color: rgba(246,242,232,0.65); }
        .wp-trip-hero-cost-value { margin: 0.15rem 0 0; font-size: 1.4rem; color: var(--parchment); }

        .wp-trip-tabs { display: flex; align-items: center; justify-content: space-between; gap: 0.6rem; border-bottom: 1px solid var(--hairline); margin-bottom: 1.6rem; flex-wrap: wrap; }
        .wp-trip-tab-row { display: flex; gap: 0.3rem; }
        .wp-trip-tab { padding: 0.7rem 1.1rem; font-size: 0.85rem; color: var(--ink-soft); display: flex; align-items: center; gap: 0.4rem; background: none; border: none; font-family: 'Work Sans', sans-serif; cursor: default; }
        button.wp-trip-tab { cursor: pointer; }
        .wp-trip-tab-active { color: var(--navy); font-weight: 600; border-bottom: 2.5px solid var(--navy); }
        .wp-trip-tab-badge { font-size: 0.62rem; background: var(--parchment-deep); color: var(--ink-soft); padding: 0.1rem 0.5rem; border-radius: 999px; }
        .wp-trip-header-actions { display: flex; gap: 0.6rem; padding-bottom: 0.7rem; flex-wrap: wrap; }
        .wp-trip-header-btn { display: flex; align-items: center; gap: 0.4rem; background: #fff; border: 1px solid var(--hairline); border-radius: 10px; padding: 0.55rem 0.9rem; font-size: 0.78rem; font-weight: 600; color: var(--navy); cursor: pointer; }

        .wp-trip-route-layout { display: flex; gap: 2rem; align-items: flex-start; margin-bottom: 1.6rem; flex-wrap: wrap; }
        .wp-trip-timeline-col { flex: 1; min-width: 280px; position: relative; padding-left: 2.3rem; }
        .wp-trip-route-line { position: absolute; left: 0.85rem; top: 1.7rem; bottom: 3rem; width: 1px; background: var(--hairline); }
        .wp-trip-insert-link { display: flex; align-items: center; gap: 0.35rem; background: none; border: none; color: var(--ink-soft); font-size: 0.74rem; opacity: 0.65; cursor: pointer; padding: 0 0 0.8rem; margin-left: -0.1rem; }
        .wp-trip-insert-link:hover { opacity: 1; color: var(--gold); }
        .wp-trip-entry { position: relative; display: flex; gap: 1.2rem; margin-bottom: 0.4rem; }
        .wp-trip-entry-dot { position: absolute; left: -2.3rem; top: 0.3rem; width: 15px; height: 15px; border-radius: 50%; background: var(--hairline); border: 3px solid var(--parchment); }
        .wp-trip-entry-dot-active { background: var(--gold); box-shadow: 0 0 0 1px var(--gold); }
        .wp-trip-entry-photo { width: 150px; height: 108px; border-radius: 14px; flex-shrink: 0; background-size: cover; }
        .wp-trip-entry-body { flex: 1; padding-top: 0.2rem; min-width: 0; }
        .wp-trip-entry-head { display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.5rem; flex-wrap: wrap; }
        .wp-trip-entry-days { display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.8rem; color: var(--ink-soft); background: var(--parchment); border-radius: 999px; padding: 0.25rem 0.35rem 0.25rem 0.6rem; }
        .wp-trip-date-range-hint { margin: -0.3rem 0 0.7rem; font-size: 0.72rem; color: var(--ink-soft); opacity: 0.8; }
        .wp-trip-chips-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.7rem; }
        .wp-trip-chip { display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.76rem; background: #fff; border: 1px solid var(--hairline); padding: 0.28rem 0.7rem; border-radius: 999px; }
        .wp-trip-chip-remove { background: none; border: none; cursor: pointer; color: var(--ink-soft); display: flex; padding: 0; }
        .wp-trip-chip-add { background: var(--parchment); border: 1px dashed var(--hairline); color: var(--ink-soft); cursor: pointer; }

        .wp-trip-panel-row { display: flex; gap: 0.5rem; position: relative; flex-wrap: nowrap; }
        .wp-trip-panel-btn { display: flex; align-items: center; justify-content: center; gap: 0.35rem; flex: 1 1 0; min-width: 0; background: #fff; border: 1px solid var(--hairline); border-radius: 10px; padding: 0.5rem 0.5rem; font-size: 0.74rem; font-weight: 500; color: var(--ink-soft); cursor: pointer; text-align: center; white-space: normal; line-height: 1.2; }
        .wp-trip-panel-btn svg { flex-shrink: 0; }
        @media (max-width: 380px) {
          .wp-trip-panel-row { gap: 0.35rem; }
          .wp-trip-panel-btn { font-size: 0.68rem; padding: 0.45rem 0.3rem; gap: 0.25rem; }
        }
        .wp-trip-panel-btn-active { background: var(--navy-subtle); border: 1.5px solid var(--navy); color: var(--navy); font-weight: 600; }
        .wp-trip-panel-btn-empty { border-style: dashed; }
        .wp-trip-panel-connector { position: absolute; top: 100%; width: 12px; height: 12px; background: #fff; border-left: 1.5px solid var(--navy); border-top: 1.5px solid var(--navy); transform: rotate(45deg); margin-top: -1px; }
        .wp-trip-panel-box { background: #fff; border: 1.5px solid var(--navy); border-radius: 12px; padding: 1.2rem 1.35rem; margin-top: 0.75rem; position: relative; }
        .wp-trip-panel-box-label { margin: 0 0 0.8rem; font-size: 0.66rem; letter-spacing: 0.03em; text-transform: uppercase; color: var(--navy); font-weight: 600; padding-right: 1.6rem; }
        .wp-trip-summary-line { display: block; width: 100%; text-align: left; background: none; border: none; padding: 0.4rem 0.1rem; margin-top: 0.2rem; font-size: 0.82rem; color: var(--ink); cursor: pointer; }
        .wp-trip-summary-line:hover { color: var(--navy); }
        .wp-trip-panel-close { position: absolute; top: 0.85rem; right: 0.85rem; background: none; border: none; color: var(--ink-soft); cursor: pointer; padding: 0.2rem; line-height: 0; }
        .wp-trip-panel-close:hover { color: var(--ink); }

        .wp-trip-transit-summary-row { display: flex; align-items: center; gap: 0.6rem; margin: 0.7rem 0 0.7rem -2.3rem; padding-left: 2.3rem; cursor: pointer; }
        .wp-trip-transit-summary-row:hover .wp-trip-transit-summary-text, .wp-trip-transit-summary-row:hover .wp-trip-transit-summary-edit { color: var(--ink); }
        .wp-trip-transit-summary-text { font-size: 0.76rem; color: var(--ink-soft); flex: 1; }
        .wp-trip-transit-summary-edit { background: none; border: none; color: var(--ink-soft); font-size: 0.72rem; text-decoration: underline; cursor: pointer; }

        .wp-trip-map-panel { width: 340px; flex-shrink: 0; background: #fff; border: 1px solid var(--hairline); border-radius: 16px; overflow: hidden; position: sticky; top: 20px; }
        .wp-trip-map-label { margin: 0; position: absolute; z-index: 400; font-size: 0.68rem; color: #5B6B47; background: rgba(255,255,255,0.75); padding: 0.2rem 0.55rem; border-radius: 999px; margin: 0.7rem 0 0 0.7rem; }
        .wp-trip-map, .wp-trip-map-empty { height: 340px; background: #DCE8DA; }
        .wp-trip-map-empty { display: flex; align-items: center; justify-content: center; }
        .wp-trip-map-note { margin: 0; padding: 0.7rem 0.9rem; font-size: 0.7rem; color: var(--ink-soft); border-top: 1px solid var(--hairline); }
        @media (max-width: 900px) { .wp-trip-map-panel { width: 100%; position: static; } }

        .wp-trip-days-tab { margin-bottom: 1.6rem; }
        .wp-trip-day-pills { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.3rem; }
        .wp-trip-day-pill { background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.5rem 1.05rem; font-size: 0.82rem; font-weight: 500; color: var(--ink-soft); cursor: pointer; }
        .wp-trip-day-pill-active { background: var(--navy); border-color: var(--navy); color: var(--parchment); font-weight: 600; }
        .wp-trip-day-header-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.6rem; }
        .wp-trip-day-suggestions { margin-bottom: 1.1rem; }
        .wp-trip-day-suggestions-label { margin: 0 0 0.5rem; font-size: 0.72rem; color: var(--ink-soft); }
        .wp-trip-day-city { margin: 0; font-size: 1.25rem; font-weight: 600; }
        .wp-trip-day-view-toggle { display: flex; background: var(--parchment-deep); border-radius: 8px; padding: 0.2rem; gap: 0.2rem; }
        .wp-trip-day-view-btn { background: none; border: none; padding: 0.4rem 0.9rem; font-size: 0.78rem; font-weight: 600; color: var(--ink-soft); border-radius: 6px; cursor: pointer; }
        .wp-trip-day-view-btn-active { background: #fff; color: var(--navy); box-shadow: 0 1px 2px rgba(20,32,53,0.08); }
        .wp-trip-day-list { background: #fff; border: 1px solid var(--hairline); border-radius: 14px; padding: 1.2rem 1.3rem; }
        .wp-trip-day-list-empty { margin: 0 0 0.8rem; font-size: 0.85rem; color: var(--ink-soft); }
        .wp-trip-day-activity-row { display: flex; align-items: center; gap: 0.7rem; padding: 0.55rem 0; border-bottom: 1px solid var(--parchment-deep); }
        .wp-trip-day-activity-time { font-size: 0.82rem; color: var(--gold); min-width: 3.2rem; }
        .wp-trip-day-activity-name { flex: 1; font-size: 0.9rem; }
        .wp-day-map-empty-text { font-size: 0.82rem; color: var(--ink-soft); padding: 0 1rem; text-align: center; }

        .wp-trip-bookings-tab { margin-bottom: 1.6rem; }
        .wp-trip-booking-section { background: #fff; border: 1px solid var(--hairline); border-radius: 14px; padding: 1.2rem 1.3rem; margin-bottom: 1.1rem; }
        .wp-trip-booking-section-title { margin: 0 0 0.9rem; font-size: 1.05rem; font-weight: 600; }
        .wp-trip-booking-card { border: 1px solid var(--parchment-deep); border-radius: 10px; padding: 0.85rem 1rem; margin-bottom: 0.7rem; }
        .wp-trip-booking-card:last-child { margin-bottom: 0; }
        .wp-trip-booking-card-head { display: flex; align-items: center; justify-content: space-between; gap: 0.7rem; flex-wrap: wrap; margin-bottom: 0.6rem; }
        .wp-trip-booking-route { font-size: 0.88rem; font-weight: 500; }
        .wp-trip-confirm-toggle { font-size: 0.7rem; font-weight: 600; padding: 0.3rem 0.7rem; border-radius: 11px; border: 1px solid var(--hairline); background: var(--parchment); color: var(--ink-soft); cursor: pointer; white-space: nowrap; }
        .wp-trip-confirm-toggle-on { background: #E4EFE9; border-color: #3F8F6F; color: #2E6B52; }
        .wp-trip-view-in-route-link { background: none; border: none; color: var(--ink-soft); font-size: 0.85rem; text-decoration: underline; cursor: pointer; padding: 0; }
        .wp-trip-card:hover { border-color: var(--gold); }
        .wp-trip-card-top { display: flex; justify-content: space-between; align-items: center; gap: 0.6rem; }
        .wp-trip-card-name { font-size: 1.02rem; display: flex; align-items: center; gap: 0.5rem; }
        .wp-trip-card-meta { font-size: 0.82rem; color: var(--ink-soft); margin: 0.3rem 0 0; }
        .wp-trip-status-badge { font-size: 0.72rem; background: var(--parchment); color: var(--ink-soft); padding: 0.2rem 0.6rem; border-radius: 999px; white-space: nowrap; }
        .wp-trip-status-done { background: #E3EDE1; color: #3E6B3A; }
        .wp-field-label { display: block; font-size: 0.75rem; color: var(--ink-soft); margin: 0.7rem 0 0.25rem; }
        .wp-trip-country-results { background: #fff; border: 1px solid var(--hairline); border-radius: 10px; margin-top: -0.2rem; margin-bottom: 0.3rem; overflow: hidden; }
        .wp-trip-country-row { display: flex; align-items: center; gap: 0.5rem; width: 100%; text-align: left; background: none; border: none; border-top: 1px solid var(--hairline); padding: 0.5rem 0.7rem; font-size: 0.88rem; cursor: pointer; }
        .wp-trip-country-row:first-child { border-top: none; }
        .wp-trip-country-row:hover { background: var(--parchment); }
        .wp-trip-date-row { display: flex; gap: 0.5rem; }
        .wp-trip-days-hint { font-size: 0.78rem; color: var(--ink-soft); margin: 0.3rem 0 0; }
        .wp-trip-back { display: flex; align-items: center; gap: 0.3rem; background: none; border: none; font-size: 0.85rem; color: var(--ink-soft); cursor: pointer; padding: 0; margin-bottom: 1rem; }
        .wp-trip-detail-header { margin-bottom: 1rem; }
        .wp-trip-cost-row { display: flex; gap: 0.7rem; margin-bottom: 1.2rem; }
        .wp-trip-cost-box { flex: 1; background: var(--parchment); border-radius: 10px; padding: 0.6rem 0.8rem; }
        .wp-trip-cost-label { font-size: 0.7rem; color: var(--ink-soft); margin: 0; }
        .wp-trip-cost-value { font-size: 1.2rem; margin: 0.1rem 0 0; }
        .wp-trip-stop-card { background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.8rem 1rem; margin-bottom: 0.4rem; }
        .wp-trip-stop-top { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.4rem; }
        .wp-trip-city-input { flex: 1; border: none; border-bottom: 1px solid var(--hairline); font-size: 0.98rem; padding: 0.2rem 0; background: none; }
        .wp-trip-city-input:focus { outline: none; border-color: var(--gold); }
        .wp-trip-day-range { font-size: 0.75rem; color: var(--ink-soft); white-space: nowrap; }
        .wp-trip-remove-btn { background: none; border: none; color: var(--ink-soft); cursor: pointer; padding: 0.15rem; display: flex; flex-shrink: 0; }
        .wp-trip-remove-btn:hover { color: #B5453D; }
        .wp-trip-highlight-row { display: flex; align-items: center; gap: 0.5rem; padding: 0.35rem 0; border-top: 1px solid var(--hairline); }
        .wp-trip-highlight-text { flex: 1; font-size: 0.85rem; }
        .wp-trip-add-highlight-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.4rem; }
        .wp-trip-highlight-input { flex: 1 1 100px; min-width: 0; font-size: 0.9rem; padding: 0.6rem 0.75rem; border: 1px solid var(--hairline); border-radius: 8px; }
        @media (max-width: 640px) {
          .wp-trip-add-highlight-row { flex-direction: column; align-items: stretch; gap: 0.6rem; }
          .wp-trip-add-highlight-row input.wp-trip-highlight-input { flex: 1 1 auto; width: 100%; box-sizing: border-box; }
          .wp-trip-add-highlight-row .wp-trip-add-btn { align-self: flex-end; }
          .wp-trip-panel-box { padding: 1.1rem; }
        }
        .wp-trip-add-btn { background: var(--parchment); border: 1px solid var(--hairline); border-radius: 8px; padding: 0.4rem 0.6rem; cursor: pointer; display: flex; align-items: center; }
        .wp-trip-suggestions { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; }
        .wp-trip-suggestions-label { margin: 0.9rem 0 0.4rem; font-size: 0.72rem; color: var(--ink-soft); }
        .wp-trip-suggestion-chip { display: flex; align-items: center; gap: 0.25rem; font-size: 0.76rem; background: var(--parchment); border: 1px solid var(--hairline); border-radius: 999px; padding: 0.25rem 0.6rem; cursor: pointer; color: var(--ink-soft); }
        .wp-trip-suggestion-chip:hover { border-color: var(--gold); color: var(--ink); }
        .wp-trip-transit-row { display: flex; flex-wrap: wrap; gap: 0.4rem; padding: 0.5rem 0.2rem; margin-left: 1rem; border-left: 2px dashed var(--hairline); }
        .wp-trip-transit-select, .wp-trip-transit-input { flex: none; font-size: 0.9rem; padding: 0.6rem 0.75rem; border: 1px solid var(--hairline); border-radius: 10px; background: #fff; min-width: 0; width: 100%; }
        .wp-trip-transit-select { width: 100%; }
        .wp-trip-transit-input { width: 100%; }
        .wp-trip-add-stop-btn { display: flex; align-items: center; justify-content: center; gap: 0.4rem; width: 100%; background: none; border: 1px dashed var(--hairline); border-radius: 10px; padding: 0.6rem; font-size: 0.85rem; color: var(--ink-soft); cursor: pointer; margin: 0.6rem 0 1.2rem; }
        .wp-trip-add-stop-btn:hover { border-color: var(--gold); color: var(--ink); }
        .wp-trip-footer-actions { display: flex; gap: 0.6rem; flex-wrap: wrap; }
        .wp-trip-delete-btn { background: none; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.55rem 1.1rem; font-size: 0.85rem; color: #B5453D; cursor: pointer; }
        .wp-trip-subsection { margin-top: 0.7rem; padding-top: 0.6rem; border-top: 1px solid var(--hairline); }
        .wp-trip-subsection-label { font-size: 0.72rem; color: var(--ink-soft); margin: 0 0 0.35rem; text-transform: uppercase; letter-spacing: 0.03em; }
        .wp-trip-typical-hint { font-size: 0.72rem; color: var(--ink-soft); margin: 0.2rem 0 0.6rem 1.2rem; }
        .wp-trip-export-btn { display: flex; align-items: center; gap: 0.4rem; background: none; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.5rem 1rem; font-size: 0.82rem; color: var(--ink); cursor: pointer; margin-bottom: 1.2rem; }
        .wp-trip-export-btn:hover { border-color: var(--gold); }
        .wp-trip-action-row { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1.2rem; }
        .wp-trip-action-row .wp-trip-export-btn { margin-bottom: 0; }
        .wp-trip-insert-before-btn { display: flex; align-items: center; gap: 0.3rem; width: 100%; background: none; border: none; font-size: 0.7rem; color: var(--ink-soft); cursor: pointer; padding: 0.25rem 0.4rem; opacity: 0.55; }
        .wp-trip-insert-before-btn:hover { opacity: 1; color: var(--gold); }
        .wp-trip-day-range-edit { display: flex; align-items: center; gap: 0.25rem; font-size: 0.75rem; color: var(--ink-soft); white-space: nowrap; }
        .wp-trip-day-num { width: 2.6rem; font-size: 0.75rem; padding: 0.2rem 0.3rem; border: 1px solid var(--hairline); border-radius: 6px; text-align: center; }
        .wp-trip-transit-num { flex: 0 0 3.4rem; text-align: center; }

        .wp-trip-notes-box { background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 1.1rem 1.2rem 0.4rem; margin: 0.2rem 0 1.2rem; }
        .wp-trip-notes-title { font-size: 1rem; margin: 0 0 0.15rem; }
        .wp-trip-notes-subtitle { font-size: 0.78rem; color: var(--ink-soft); margin: 0 0 1.1rem; }
        .wp-trip-timeline { position: relative; padding-left: 1.35rem; }
        .wp-trip-timeline-line { position: absolute; left: 0.3rem; top: 0.35rem; bottom: 1rem; width: 1px; background: var(--hairline); }
        .wp-trip-timeline-entry { position: relative; padding-bottom: 1.2rem; }
        .wp-trip-timeline-dot { position: absolute; left: -1.35rem; top: 0.15rem; width: 11px; height: 11px; border-radius: 50%; background: var(--hairline); }
        .wp-trip-timeline-dot-filled { background: var(--gold); }
        .wp-trip-timeline-day { font-size: 0.85rem; margin: 0 0 0.35rem; }
        .wp-trip-timeline-city { color: var(--ink-soft); }
        .wp-trip-timeline-note { border-left: 2px solid var(--gold); padding: 0.1rem 0 0.1rem 0.75rem; margin: 0; font-size: 0.85rem; color: #3a352b; cursor: pointer; white-space: pre-wrap; }
        .wp-trip-timeline-note-readonly { cursor: default; }
        .wp-trip-timeline-add { font-size: 0.78rem; color: var(--ink-soft); background: none; border: none; padding: 0; cursor: pointer; text-align: left; }
        .wp-trip-timeline-add:hover { color: var(--gold); }
        .wp-trip-timeline-input { width: 100%; font-family: 'Work Sans', sans-serif; font-size: 0.85rem; padding: 0.5rem 0.6rem; border: 1px solid var(--hairline); border-radius: 8px; resize: vertical; background: #fff; color: var(--ink); box-sizing: border-box; }
        .wp-trip-timeline-input:focus { outline: none; border-color: var(--gold); }
        .wp-trip-city-readonly { flex: 1; font-size: 0.98rem; }

        .wp-trip-share-box { background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.9rem 1.1rem; margin-bottom: 1.2rem; }
        .wp-trip-share-row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
        .wp-trip-share-title { font-size: 0.95rem; margin: 0; }
        .wp-trip-share-desc { font-size: 0.78rem; color: var(--ink-soft); margin: 0.2rem 0 0; }
        .wp-trip-share-toggle { flex-shrink: 0; width: 42px; height: 24px; border-radius: 999px; background: var(--hairline); border: none; position: relative; cursor: pointer; padding: 0; transition: background 0.15s ease; }
        .wp-trip-share-toggle-on { background: var(--gold); }
        .wp-trip-share-toggle-knob { position: absolute; top: 3px; left: 3px; width: 18px; height: 18px; border-radius: 50%; background: #fff; transition: transform 0.15s ease; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }
        .wp-trip-share-toggle-on .wp-trip-share-toggle-knob { transform: translateX(18px); }
        .wp-trip-share-link-row { display: flex; gap: 0.4rem; margin-top: 0.8rem; }
        .wp-trip-share-link-input { flex: 1; min-width: 0; font-size: 0.8rem; padding: 0.5rem 0.7rem; border: 1px solid var(--hairline); border-radius: 8px; background: var(--parchment); color: var(--ink-soft); }

        .wp-shared-trip-banner { background: var(--parchment); border: 1px solid var(--hairline); border-radius: 10px; padding: 0.6rem 0.9rem; font-size: 0.82rem; color: var(--ink-soft); margin-bottom: 1.2rem; text-align: center; }
        .wp-map-list-row:hover { text-decoration: underline; }

        .wp-modal-overlay { position: fixed; inset: 0; background: rgba(20,32,53,0.45); display: flex; align-items: center; justify-content: center; z-index: 1000; padding: 1.2rem; }
        .wp-auth-modal { position: relative; background: #fff; border-radius: 14px; padding: 2rem 1.8rem; max-width: 380px; width: 100%; box-shadow: 0 20px 50px rgba(20,32,53,0.25); }
        .wp-modal-close { position: absolute; top: 1rem; right: 1rem; background: none; border: none; cursor: pointer; color: var(--ink-soft); padding: 0.2rem; }
        .wp-auth-title { font-size: 1.4rem; font-weight: 600; margin: 0 0 0.4rem; }
        .wp-auth-subtitle { font-size: 0.86rem; color: var(--ink-soft); line-height: 1.45; margin: 0 0 1.3rem; }
        .wp-google-btn { display: flex; align-items: center; justify-content: center; gap: 0.6rem; width: 100%; background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.65rem 1rem; font-family: 'Work Sans', sans-serif; font-size: 0.9rem; font-weight: 600; color: var(--ink); cursor: pointer; }
        .wp-google-btn:hover { background: var(--parchment); }
        .wp-auth-divider { display: flex; align-items: center; text-align: center; color: var(--ink-soft); font-size: 0.78rem; margin: 1rem 0; }
        .wp-auth-divider::before, .wp-auth-divider::after { content: ""; flex: 1; border-top: 1px solid var(--hairline); }
        .wp-auth-divider span { padding: 0 0.7rem; }
        .wp-auth-input { width: 100%; background: var(--parchment); border: 1px solid var(--hairline); border-radius: 8px; padding: 0.7rem 0.9rem; font-family: 'Work Sans', sans-serif; font-size: 0.9rem; margin-bottom: 0.7rem; color: var(--ink); }
        .wp-auth-error { font-size: 0.82rem; color: #B5453D; margin: -0.2rem 0 0.7rem; }
        .wp-auth-switch { display: block; width: 100%; text-align: center; background: none; border: none; margin-top: 1rem; font-family: 'Work Sans', sans-serif; font-size: 0.82rem; color: var(--ink-soft); text-decoration: underline; cursor: pointer; }

        .wp-about-top { display: flex; gap: 1.3rem; align-items: flex-start; flex-wrap: wrap; margin-bottom: 1rem; }
        .wp-about-photo-img { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 1px solid var(--hairline); flex-shrink: 0; }
        .wp-about-bio { font-size: 0.98rem; line-height: 1.65; max-width: 60ch; margin: 0 0 1rem; }

        .wp-newsletter-card { max-width: 480px; min-height: 80px; }
        .wp-newsletter-form { max-width: 420px; display: flex; flex-direction: column; }
        .wp-newsletter-success { max-width: 420px; background: #fff; border: 1px solid var(--hairline); border-radius: 10px; padding: 1rem 1.2rem; color: var(--ink); font-size: 0.95rem; }

        .wp-coming-soon { text-align: center; padding: 2.5rem 1rem 1rem; }
        .wp-coming-soon-visual { width: 170px; margin: 0 auto; }
        .wp-soon-svg { width: 100%; height: auto; display: block; }

        .wp-detail-tagline { font-weight: 500; font-size: 1.3rem; color: #463F30; margin: 0.5rem 0 1rem; max-width: 50ch; line-height: 1.45; }
        .wp-chip-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.3rem; }
        .wp-chip { background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.3rem 0.8rem; font-size: 0.8rem; color: var(--ink); }

        .wp-good-to-know { background: #fff; border: 1px solid var(--hairline); border-radius: 3px; padding: 1.1rem 1.2rem; margin-bottom: 1.9rem; }
        .wp-gtk-grid { display: grid; grid-template-columns: 1fr; gap: 1rem 1.4rem; margin-top: 0.7rem; }
        @media (min-width: 520px) { .wp-gtk-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (min-width: 760px) { .wp-gtk-grid { grid-template-columns: repeat(3, 1fr); } }

        .wp-detail-anchor-nav { display: flex; gap: 0.3rem; overflow-x: auto; -webkit-overflow-scrolling: touch; position: sticky; top: 0; z-index: 50; background: var(--parchment); padding: 0.7rem 0; margin-bottom: 1.4rem; border-bottom: 1px solid var(--hairline); scrollbar-width: none; }
        .wp-detail-anchor-nav::-webkit-scrollbar { display: none; }
        .wp-detail-anchor { flex-shrink: 0; background: none; border: none; padding: 0.5rem 0.9rem; border-radius: 8px; font-size: 0.85rem; font-weight: 500; color: var(--ink-soft); cursor: pointer; white-space: nowrap; }
        .wp-detail-anchor:hover { background: var(--parchment-deep); color: var(--ink); }
        .wp-detail-anchor-active { background: var(--navy-subtle); color: var(--navy); font-weight: 600; }

        .wp-accordion { margin-top: 0.7rem; border-top: 1px solid var(--hairline); }
        .wp-accordion-row { border-bottom: 1px solid var(--hairline); }
        .wp-accordion-trigger { display: flex; align-items: center; gap: 0.7rem; width: 100%; background: none; border: none; text-align: left; padding: 0.9rem 0.2rem; cursor: pointer; font-family: 'Work Sans', sans-serif; min-height: 44px; }
        .wp-accordion-trigger-label { flex: 1; font-size: 0.92rem; color: var(--ink); font-weight: 500; }
        .wp-faq-q-label { font-weight: 600; }
        .wp-accordion-chevron { color: var(--ink-soft); transform: rotate(90deg); transition: transform 0.15s ease; flex-shrink: 0; }
        .wp-accordion-chevron-open { transform: rotate(-90deg); }
        .wp-accordion-content { padding: 0 0.2rem 1.1rem 2.6rem; font-size: 0.9rem; color: #3a352b; line-height: 1.55; }
        .wp-faq-q-label ~ .wp-accordion-chevron { }
        .wp-accordion-row:has(.wp-faq-q-label) .wp-accordion-content { padding-left: 0.2rem; }
        .wp-gtk-label { font-size: 0.78rem; color: var(--ink-soft); margin-bottom: 0.2rem; }
        .wp-gtk-value { font-size: 0.9rem; line-height: 1.45; }

        .wp-food-grid { display: grid; grid-template-columns: 1fr; gap: 0.8rem; }
        @media (min-width: 560px) { .wp-food-grid { grid-template-columns: repeat(2, 1fr); } }
        .wp-food-item { background: #fff; border: 1px solid var(--hairline); border-radius: 3px; padding: 0.85rem 1rem; }
        .wp-food-name { font-weight: 600; font-size: 0.92rem; margin-bottom: 0.25rem; }
        .wp-food-desc { font-size: 0.86rem; color: #4a4436; line-height: 1.5; }

        .wp-map { width: 100%; height: 280px; border-radius: 4px; border: 1px solid var(--hairline); margin-bottom: 1.1rem; background: #EDE6D4; }
        .wp-map-pin-inner { width: 24px; height: 24px; border-radius: 50%; color: #fff; font-size: 0.72rem; font-weight: 700; display: flex; align-items: center; justify-content: center; border: 2px solid #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.35); font-family: 'Work Sans', sans-serif; }

        .wp-day-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.4rem; }
        .wp-day-tag { font-size: 0.74rem; background: #EDE6D4; color: #4a4436; padding: 0.15rem 0.55rem; border-radius: 999px; }
        .wp-day-tag-book { background: #16233B; color: #F3EDE0; }
        .wp-day-extra { font-size: 0.82rem; color: #4a4436; line-height: 1.5; margin-top: 0.4rem; }
        .wp-day-extra strong { color: var(--ink); }

        .wp-days-reason { font-size: 0.86rem; color: var(--ink-soft); line-height: 1.5; margin: 0.4rem 0 1.1rem; max-width: 62ch; }

        .wp-faq-wrap { margin-top: 2rem; }
        .wp-faq-item { background: #fff; border: 1px solid var(--hairline); border-radius: 3px; padding: 0.9rem 1.1rem; margin-top: 0.8rem; }
        .wp-faq-q { font-weight: 600; font-size: 0.94rem; margin-bottom: 0.35rem; color: var(--ink); }
        .wp-faq-a { font-size: 0.86rem; line-height: 1.55; color: #4a4436; }

        .wp-pairs-wrap { margin-top: 2rem; }
        .wp-pairs-row { display: flex; flex-wrap: wrap; gap: 0.7rem; }
        .wp-pairs-card { display: flex; align-items: center; gap: 0.5rem; background: #fff; border: 1px solid var(--hairline); border-radius: 11px; padding: 0.5rem 0.9rem 0.5rem 0.7rem; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.88rem; color: var(--ink); }
        .wp-pairs-card:hover { background: #FBF8F1; }

        .wp-footer { margin-top: 3.5rem; padding-top: 2rem; border-top: 1px solid var(--hairline); }
        .wp-footer-top { display: flex; flex-wrap: wrap; gap: 2.5rem; justify-content: space-between; margin-bottom: 1.6rem; }
        .wp-footer-brand { display: flex; gap: 0.65rem; max-width: 340px; }
        .wp-footer-brand-name { font-size: 1.05rem; font-weight: 600; margin-bottom: 0.25rem; }
        .wp-footer-tagline { font-size: 0.82rem; color: var(--ink-soft); line-height: 1.45; }
        .wp-footer-col { display: flex; flex-direction: column; gap: 0.5rem; min-width: 120px; }
        .wp-footer-col-title { font-size: 0.78rem; color: var(--ink-soft); margin-bottom: 0.2rem; }
        .wp-footer-link { background: none; border: none; padding: 0; text-align: left; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.88rem; color: var(--ink); text-decoration: none; }
        .wp-footer-link:hover { color: var(--navy); text-decoration: underline; }
        .wp-footer-bottom { display: flex; flex-wrap: wrap; gap: 0.5rem 1.2rem; justify-content: space-between; padding-top: 1.3rem; border-top: 1px solid var(--hairline); font-size: 0.78rem; color: var(--ink-soft); }
        .wp-footer-org-link { color: var(--ink-soft); text-decoration: underline; }
        .wp-footer-org-link:hover { color: var(--navy); }
      `}</style>

      <div className="wp-shell">
        <nav className="wp-nav">
          <button className="wp-nav-brand" onClick={goToContinents}>
            <div className="wp-brand-mark" style={{ width: 24, height: 24 }}><Compass size={13} style={{ color: "#F3EDE0" }} /></div>
            Waypoint
          </button>
          <div className="wp-nav-links">
            <button className={"wp-nav-link" + ((view === "continents" || view === "countries" || view === "detail") ? " wp-nav-link-active" : "")} onClick={goToContinents}>{T.home}</button>
            {firebaseReady && (
              <button className={"wp-nav-link" + (view === "map" ? " wp-nav-link-active" : "")} onClick={() => goToStatic("map")}>{T.myMap}</button>
            )}
            {firebaseReady && (
              <button className={"wp-nav-link" + ((view === "trips" || view === "trip-detail") ? " wp-nav-link-active" : "")} onClick={() => { setActiveTripId(null); goToStatic("trips"); }}>{T.myTrips}</button>
            )}
            <button className={"wp-nav-link" + (view === "articles" ? " wp-nav-link-active" : "")} onClick={() => goToStatic("articles")}>{T.articles}</button>
            <button className={"wp-nav-link" + (view === "products" ? " wp-nav-link-active" : "")} onClick={() => goToStatic("products")}>{T.products}</button>
            <button className={"wp-nav-link" + (view === "newsletter" ? " wp-nav-link-active" : "")} onClick={() => goToStatic("newsletter")}>{T.newsletter}</button>
            <button className={"wp-nav-link" + (view === "about" ? " wp-nav-link-active" : "")} onClick={() => goToStatic("about")}>{T.aboutMe}</button>
            <span className="wp-lang-toggle">
              <button className={"wp-lang-btn" + (lang === "en" ? " wp-lang-btn-active" : "")} onClick={() => setLang("en")}>EN</button>
              <span className="wp-lang-sep">/</span>
              <button className={"wp-lang-btn" + (lang === "pt" ? " wp-lang-btn-active" : "")} onClick={() => setLang("pt")}>PT</button>
            </span>
            {firebaseReady && !authLoading && (
              user ? (
                <span className="wp-user-menu-wrap">
                  <button className="wp-user-chip" onClick={() => setShowUserMenu((s) => !s)}>
                    <UserIcon size={14} />
                    <span className="wp-user-email">{user.email ? user.email.split("@")[0] : "Account"}</span>
                  </button>
                  {showUserMenu && (
                    <div className="wp-user-dropdown">
                      <button className="wp-user-dropdown-item" onClick={signOutUser}><LogOutIcon size={14} /> {T.signOut}</button>
                    </div>
                  )}
                </span>
              ) : (
                <button className="wp-signin-btn" onClick={() => openAuthModal("signin")}>{T.signIn}</button>
              )
            )}
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: "0.6rem" }}>
          {firebaseReady && !authLoading && (
            user ? (
              <button className="wp-nav-account-badge wp-nav-account-badge-in" onClick={() => setMobileMenuOpen(true)} aria-label={T.signedInAs + " " + (user.email || "")} title={user.email || ""}>
                {(user.email || "?").charAt(0).toUpperCase()}
              </button>
            ) : (
              <button className="wp-nav-account-badge wp-nav-account-badge-out" onClick={() => openAuthModal("signin")} aria-label={T.signIn} title={T.notSignedIn}>
                <UserIcon size={15} />
              </button>
            )
          )}
          <button
            className="wp-hamburger-btn"
            ref={menuTriggerRef}
            onClick={() => setMobileMenuOpen(true)}
            aria-label={T.openMenu}
            aria-haspopup="true"
            aria-expanded={mobileMenuOpen}
          >
            <MenuIcon size={22} />
          </button>
          </div>
        </nav>

        {mobileMenuOpen && (
          <div className="wp-mobile-menu-overlay" onClick={() => setMobileMenuOpen(false)}>
            <div
              className="wp-mobile-menu-panel"
              ref={menuPanelRef}
              role="dialog"
              aria-modal="true"
              aria-label={T.menuLabel}
              onClick={(e) => e.stopPropagation()}
            >
              <div className="wp-mobile-menu-head">
                <button className="wp-nav-brand" onClick={() => { goToContinents(); setMobileMenuOpen(false); }}>
                  <div className="wp-brand-mark" style={{ width: 24, height: 24 }}><Compass size={13} style={{ color: "#F3EDE0" }} /></div>
                  Waypoint
                </button>
                <button className="wp-mobile-menu-close" onClick={() => setMobileMenuOpen(false)} aria-label={T.closeMenu}>
                  <X size={18} />
                </button>
              </div>

              <div className="wp-mobile-menu-scroll">
                <p className="wp-mobile-menu-label">{T.menuLabel}</p>
                <button className={"wp-mobile-menu-item" + ((view === "continents" || view === "countries" || view === "detail") ? " wp-mobile-menu-item-active" : "")} onClick={() => { goToContinents(); setMobileMenuOpen(false); }}>
                  <HomeIcon size={19} /> {T.home}
                </button>
                {firebaseReady && (
                  <button className={"wp-mobile-menu-item" + (view === "map" ? " wp-mobile-menu-item-active" : "")} onClick={() => { goToStatic("map"); setMobileMenuOpen(false); }}>
                    <MapPinIcon size={19} /> {T.myMap}
                  </button>
                )}
                {firebaseReady && (
                  <button className={"wp-mobile-menu-item" + ((view === "trips" || view === "trip-detail") ? " wp-mobile-menu-item-active" : "")} onClick={() => { setActiveTripId(null); goToStatic("trips"); setMobileMenuOpen(false); }}>
                    <SuitcaseIcon size={19} /> {T.myTrips}
                  </button>
                )}
                <button className={"wp-mobile-menu-item" + (view === "articles" ? " wp-mobile-menu-item-active" : "")} onClick={() => { goToStatic("articles"); setMobileMenuOpen(false); }}>
                  <FileIcon size={19} /> {T.articles}
                </button>
                <button className={"wp-mobile-menu-item" + (view === "products" ? " wp-mobile-menu-item-active" : "")} onClick={() => { goToStatic("products"); setMobileMenuOpen(false); }}>
                  <BagIcon size={19} /> {T.products}
                </button>

                <div className="wp-mobile-menu-sep"></div>

                <button className={"wp-mobile-menu-item" + (view === "newsletter" ? " wp-mobile-menu-item-active" : "")} onClick={() => { goToStatic("newsletter"); setMobileMenuOpen(false); }}>
                  <MailIcon size={19} /> {T.newsletter}
                </button>
                <button className={"wp-mobile-menu-item" + (view === "about" ? " wp-mobile-menu-item-active" : "")} onClick={() => { goToStatic("about"); setMobileMenuOpen(false); }}>
                  <UserIcon size={19} /> {T.aboutMe}
                </button>

                <div className="wp-mobile-menu-sep"></div>

                {firebaseReady && !authLoading && (
                  user ? (
                    <button className="wp-mobile-menu-item" onClick={() => { signOutUser(); setMobileMenuOpen(false); }}>
                      <LogOutIcon size={19} /> {T.signOut}
                    </button>
                  ) : (
                    <button className="wp-mobile-menu-item" onClick={() => { openAuthModal("signin"); setMobileMenuOpen(false); }}>
                      <UserIcon size={19} /> {T.signIn}
                    </button>
                  )
                )}
                <div className="wp-mobile-menu-lang-row">
                  <span className="wp-mobile-menu-lang-label">{T.languageLabel}</span>
                  <span className="wp-lang-toggle">
                    <button className={"wp-lang-btn" + (lang === "en" ? " wp-lang-btn-active" : "")} onClick={() => setLang("en")}>EN</button>
                    <span className="wp-lang-sep">/</span>
                    <button className={"wp-lang-btn" + (lang === "pt" ? " wp-lang-btn-active" : "")} onClick={() => setLang("pt")}>PT</button>
                  </span>
                </div>
              </div>
            </div>
          </div>
        )}

        {view === "continents" && (
          <div className="wp-hero">
            <div className="wp-hero-text">
              <h1 className="wp-hero-headline">{T.heroHeadline}</h1>
              <p className="wp-tagline">{T.heroTagline}</p>

              <div className="wp-search-wrap" style={{ margin: "0 0 1.3rem" }}>
                <div className="wp-search-box">
                  <Search size={16} className="wp-search-icon" />
                  <input
                    type="text"
                    className="wp-search-input"
                    placeholder={T.searchHome}
                    aria-label={T.searchHome}
                    value={homeQuery}
                    onChange={(e) => setHomeQuery(e.target.value)}
                  />
                  {homeQuery && (
                    <button className="wp-search-clear" onClick={() => setHomeQuery("")} aria-label="Clear search">
                      <X size={14} />
                    </button>
                  )}
                </div>
              </div>

              <div className="wp-hero-features">
                <button className="wp-hero-feature-card" onClick={() => { const el = document.querySelector(".wp-continent-grid"); if (el) el.scrollIntoView({ behavior: (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) ? "auto" : "smooth" }); }}>
                  <Compass size={18} />
                  <div><b>{T.featExploreTitle}</b><span>{T.featExploreDesc}</span></div>
                </button>
                <button className="wp-hero-feature-card" onClick={() => goToStatic("map")}>
                  <MapPinIcon size={18} />
                  <div><b>{T.featTrackTitle}</b><span>{T.featTrackDesc}</span></div>
                </button>
                <button className="wp-hero-feature-card" onClick={() => goToStatic("trips")}>
                  <CalendarClock size={18} />
                  <div><b>{T.featPlanTitle}</b><span>{T.featPlanDesc}</span></div>
                </button>
              </div>

              <div className="wp-hero-stats">
                <div className="wp-hero-stat"><b>{allCountriesFlat.length}</b><span>{T.statsCountries}</span></div>
                <div className="wp-hero-stat"><b>{totalAttractions}+</b><span>{T.statsAttractions}</span></div>
                <div className="wp-hero-stat"><b>2</b><span>{T.statsLanguages}</span></div>
              </div>
            </div>
            <div className="wp-hero-visual"><HeroIllustration /></div>
          </div>
        )}

        {view !== "continents" && (
          <div className="wp-header" style={{ marginBottom: "1.6rem" }}>
            <div className="wp-brand">
              <div className="wp-brand-mark"><Compass size={16} style={{ color: "#F3EDE0" }} /></div>
              <h1 className="wp-title" style={{ fontSize: "1.4rem" }}>Waypoint</h1>
            </div>
          </div>
        )}

        {view === "continents" && !homeQuery.trim() && (
          <div className="wp-continent-grid">
            {continents.map((c) => (
              <button
                key={c.id}
                className={"wp-continent-tile wp-cont-" + c.id + (c.id === "europe" ? " wp-tile-big" : c.id === "oceania" ? " wp-tile-wide" : "")}
                style={{ "--tile-color": c.color }}
                onClick={() => goToCountries(c.id)}
              >
                <div className="wp-continent-icon"><ContinentIcon id={c.id} /></div>
                <div className="wp-continent-body">
                  <div className="wp-continent-name">{c.name}</div>
                  <div className="wp-continent-tagline">{c.tagline}</div>
                </div>
                <div className="wp-continent-count"><b>{c.countries.length}</b> {T.countries}</div>
              </button>
            ))}
          </div>
        )}

        {view === "continents" && homeQuery.trim() && (
          <div>
            {homeSearchResults.length === 0 ? (
              <p className="wp-search-empty">{T.noResultsFor} "{homeQuery}"</p>
            ) : (
              homeSearchResults.map((cty) => (
                <button key={cty.id} className="wp-country-row" style={{ "--row-color": cty.continentColor }} onClick={() => goToDetailFromSearch(cty)}>
                  <div>
                    <div className="wp-country-name"><span>{cty.flag}</span>{cty.name}<StatusDot status={countryStatuses[cty.id]} /></div>
                    <div className="wp-country-capital">{cty.continentName} · {T.capital}: {cty.capital}</div>
                  </div>
                  <ChevronRight size={18} style={{ color: "#8a8272", flexShrink: 0 }} />
                </button>
              ))
            )}
          </div>
        )}

        {view === "continents" && (nowPicks.length > 0 || quizQuestions.length > 0) && (
          <div className="wp-monthly-wrap">
            <div className="wp-monthly-eyebrow"><span className="wp-monthly-dot"></span> {T.monthlyEyebrow}</div>

            {nowPicks.length > 0 && (
              <div className="wp-now-section">
                <h2 className="wp-section-title" style={{ marginBottom: "0.2rem" }}>{T.whereToGoNow}</h2>
                <p className="wp-now-subtitle">{T.whereToGoNowSubtitle}</p>
                <div className="wp-now-grid">
                  {nowPicks.map((cty) => (
                    <button key={cty.id} className="wp-now-card" style={{ "--now-color": cty.continentColor }} onClick={() => goToDetailFromSearch(cty)}>
                      <div className="wp-now-flag">{cty.flag}</div>
                      <div className="wp-now-name">{cty.name}</div>
                      <div className="wp-now-reason">{cty.reason}</div>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {quizQuestions.length > 0 && (
              <div className="wp-quiz-section">
                {!quizStarted && (
                  <div className="wp-quiz-card wp-quiz-intro">
                    <Award size={26} style={{ color: "#FF8A3D" }} />
                    <h2 className="wp-section-title" style={{ margin: "0.6rem 0 0.2rem" }}>{T.quizTitle}</h2>
                    <p className="wp-now-subtitle" style={{ marginBottom: "1rem" }}>{T.quizSubtitle}</p>
                    <button className="wp-quiz-btn wp-quiz-btn-primary" onClick={startQuiz}>{T.quizStart}</button>
                  </div>
                )}

                {quizStarted && !quizFinished && quizQuestions[quizIndex] && (
                  <div className="wp-quiz-card">
                    <div className="wp-quiz-progress">{T.quizQuestionLabel} {quizIndex + 1} {T.quizOf} {quizQuestions.length}</div>
                    <div className="wp-quiz-clue-wrap">
                      {quizQuestions[quizIndex].clue.type === "flag" ? (
                        <div className="wp-quiz-flag-big">{quizQuestions[quizIndex].country.flag}</div>
                      ) : quizQuestions[quizIndex].clue.type === "food" ? (
                        <div className="wp-quiz-clue-food">{quizQuestions[quizIndex].clue.text}</div>
                      ) : (
                        <div className="wp-quiz-clue-text">{quizQuestions[quizIndex].clue.text}</div>
                      )}
                    </div>
                    <p className="wp-quiz-prompt">{quizPromptFor(quizQuestions[quizIndex].clue.type)}</p>
                    <div className="wp-quiz-options">
                      {quizQuestions[quizIndex].options.map((opt) => {
                        const isCorrect = opt.id === quizQuestions[quizIndex].correctId;
                        const isSelected = opt.id === quizSelected;
                        let cls = "wp-quiz-option";
                        if (quizSelected) {
                          if (isCorrect) cls += " wp-quiz-option-correct";
                          else if (isSelected) cls += " wp-quiz-option-wrong";
                        }
                        return (
                          <button key={opt.id} className={cls} onClick={() => answerQuiz(opt.id)} disabled={!!quizSelected}>
                            <span>{opt.flag}</span> {opt.name}
                          </button>
                        );
                      })}
                    </div>
                    {quizSelected && (
                      <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ marginTop: "1rem" }} onClick={nextQuizQuestion}>
                        {quizIndex + 1 >= quizQuestions.length ? T.quizSeeResults : T.quizNext}
                      </button>
                    )}
                  </div>
                )}

                {quizFinished && (
                  <div className="wp-quiz-card wp-quiz-intro">
                    <Award size={30} style={{ color: "#FF8A3D" }} />
                    <div className="wp-quiz-score">{quizScore}/{quizQuestions.length}</div>
                    <div className="wp-quiz-rank">{quizRank(quizScore)}</div>
                    <div className="wp-quiz-actions">
                      <button className="wp-quiz-btn" onClick={copyQuizResult}>
                        <Copy size={14} /> {quizCopied ? T.quizCopied : T.quizCopyResult}
                      </button>
                      <button className="wp-quiz-btn wp-quiz-btn-primary" onClick={startQuiz}>{T.quizPlayAgain}</button>
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        )}

        {view === "countries" && continent && (
          <div>
            <button className="wp-back" onClick={goToContinents}><ArrowLeft size={15} /> {T.allContinents}</button>
            <h2 className="wp-section-title" style={{ marginBottom: "1.1rem" }}>{continent.name}</h2>
            <div className="wp-search-wrap">
              <div className="wp-search-box">
                <Search size={16} className="wp-search-icon" />
                <input
                  type="text"
                  className="wp-search-input"
                  placeholder={T.searchContinent}
                  value={continentQuery}
                  onChange={(e) => setContinentQuery(e.target.value)}
                />
                {continentQuery && (
                  <button className="wp-search-clear" onClick={() => setContinentQuery("")} aria-label="Clear search">
                    <X size={14} />
                  </button>
                )}
              </div>
            </div>
            {continentSearchResults.length === 0 ? (
              <p className="wp-search-empty">{T.noResultsFor} "{continentQuery}"</p>
            ) : (
              continentSearchResults.map((cty) => (
                <button key={cty.id} className="wp-country-row" style={{ "--row-color": continent.color }} onClick={() => goToDetail(cty)}>
                  <div>
                    <div className="wp-country-name"><span>{cty.flag}</span>{cty.name}<StatusDot status={countryStatuses[cty.id]} /></div>
                    <div className="wp-country-capital">{T.capital}: {cty.capital}</div>
                  </div>
                  <ChevronRight size={18} style={{ color: "#8a8272", flexShrink: 0 }} />
                </button>
              ))
            )}
          </div>
        )}

        {view === "detail" && continent && country && (
          <div>
            <button className="wp-back" onClick={backFromDetail}><ArrowLeft size={15} /> {cameFromMap ? T.myMap : continent.name}</button>

            <div className="wp-detail-hero">
              <h2 className="wp-detail-name"><span>{country.flag}</span>{country.name}</h2>
              <div className="wp-detail-sub">{country.capital} · {continent.name}</div>
              {country.tagline && <p className="wp-detail-tagline">{country.tagline}</p>}
              {country.highlights && (
                <div className="wp-chip-row">
                  {country.highlights.map((h, i) => <span className="wp-chip" key={i}>{h}</span>)}
                </div>
              )}
              {firebaseReady && !authLoading && (
                <div className="wp-status-row" title={!user ? T.signInToTrackHint : ""}>
                  <button
                    className={"wp-status-btn wp-status-visited" + (countryStatuses[country.id] === "visited" ? " wp-status-active" : "")}
                    onClick={() => setCountryStatus(country.id, "visited")}
                  >
                    <CheckCircle size={15} /> {T.markVisited}
                  </button>
                  <button
                    className={"wp-status-btn wp-status-want" + (countryStatuses[country.id] === "want" ? " wp-status-active" : "")}
                    onClick={() => setCountryStatus(country.id, "want")}
                  >
                    <StarIcon size={14} /> {T.markWantToVisit}
                  </button>
                </div>
              )}
            </div>

            <div className="wp-detail-anchor-nav">
              <button className={"wp-detail-anchor" + (activeDetailSection === "essential" ? " wp-detail-anchor-active" : "")} onClick={() => scrollToDetailSection("essential")}>{T.essentialAnchor}</button>
              <button className={"wp-detail-anchor" + (activeDetailSection === "places" ? " wp-detail-anchor-active" : "")} onClick={() => scrollToDetailSection("places")}>{T.placesAnchor}</button>
              <button className={"wp-detail-anchor" + (activeDetailSection === "food" ? " wp-detail-anchor-active" : "")} onClick={() => scrollToDetailSection("food")}>{T.foodAnchor}</button>
              <button className={"wp-detail-anchor" + (activeDetailSection === "route" ? " wp-detail-anchor-active" : "")} onClick={() => scrollToDetailSection("route")}>{T.routeAnchor}</button>
              <button className={"wp-detail-anchor" + (activeDetailSection === "faq" ? " wp-detail-anchor-active" : "")} onClick={() => scrollToDetailSection("faq")}>{T.faqAnchor}</button>
            </div>

            <div className="wp-stat-grid">
              <StatBlock icon={Users} label={T.population} value={country.population} accent={continent.color} />
              <StatBlock icon={Languages} label={T.language} value={country.language} accent={continent.color} />
              <StatBlock icon={Coins} label={T.currency} value={country.currency} accent={continent.color} />
              <StatBlock icon={CalendarClock} label={T.bestTime} value={country.bestTime} accent={continent.color} />
            </div>

            <p className="wp-blurb">{country.blurb}</p>

            <div ref={(el) => { detailSectionRefs.current.essential = el; }} id="section-essential"></div>
            {(country.goodToKnow || country.budget || country.visa) && (
              <div className="wp-good-to-know">
                <h3 className="wp-section-title" style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}><ShieldCheck size={18} style={{ color: continent.color }} /> {T.tripEssentials}</h3>
                <div className="wp-accordion">
                  {[
                    ["budget", DollarIcon, T.dailyBudget, country.budget],
                    ["visa", FileIcon, T.visa, country.visa],
                    ["plug", PlugIcon, T.plugVoltage, country.goodToKnow && country.goodToKnow.plug],
                    ["tipping", Coins, T.tipping, country.goodToKnow && country.goodToKnow.tipping],
                    ["safety", ShieldCheck, T.safety, country.goodToKnow && country.goodToKnow.safety],
                    ["gettingAround", MapPinIcon, T.gettingAround, country.goodToKnow && country.goodToKnow.gettingAround],
                    ["gettingThere", PlaneIcon, T.gettingThere, country.goodToKnow && country.goodToKnow.gettingThere],
                  ].filter((row) => row[3]).map(([key, Icon, label, value]) => {
                    const akey = "essential:" + country.id + ":" + key;
                    const isOpen = !!openAccordion[akey];
                    return (
                      <div className="wp-accordion-row" key={key}>
                        <button className="wp-accordion-trigger" onClick={() => toggleAccordion(akey)} aria-expanded={isOpen}>
                          <Icon size={17} style={{ color: continent.color, flexShrink: 0 }} />
                          <span className="wp-accordion-trigger-label">{label}</span>
                          <ChevronRight size={15} className={"wp-accordion-chevron" + (isOpen ? " wp-accordion-chevron-open" : "")} />
                        </button>
                        {isOpen && <div className="wp-accordion-content">{value}</div>}
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            <div ref={(el) => { detailSectionRefs.current.food = el; }} id="section-food"></div>
            {country.food && (
              <div style={{ marginBottom: "1.9rem" }}>
                <h3 className="wp-section-title" style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}><Utensils size={18} style={{ color: continent.color }} /> {T.tastesOf} {country.name}</h3>
                <div className="wp-accordion">
                  {country.food.map((f, i) => {
                    const akey = "food:" + country.id + ":" + i;
                    const isOpen = !!openAccordion[akey];
                    return (
                      <div className="wp-accordion-row" key={i}>
                        <button className="wp-accordion-trigger" onClick={() => toggleAccordion(akey)} aria-expanded={isOpen}>
                          <span className="wp-accordion-trigger-label wp-faq-q-label">{f.name}</span>
                          <ChevronRight size={15} className={"wp-accordion-chevron" + (isOpen ? " wp-accordion-chevron-open" : "")} />
                        </button>
                        {isOpen && <div className="wp-accordion-content">{f.desc}</div>}
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            <div ref={(el) => { detailSectionRefs.current.places = el; }} id="section-places"></div>
            {country.attractions ? (
              <>
                <h3 className="wp-section-title">{T.topAttractions}</h3>
                <div className="wp-attractions-grid">
                  {country.attractions.map((a, i) => {
                    const akey = "attraction:" + country.id + ":" + i;
                    const isExpanded = !!openAccordion[akey];
                    const summary = truncateSummary(a.desc, 110);
                    const needsToggle = summary !== a.desc;
                    return (
                      <div key={i}>
                        <AttractionImage title={a.wiki} alt={a.name} />
                        <div className="wp-attraction-name">{a.name}</div>
                        <div className="wp-attraction-desc">{isExpanded ? a.desc : summary}</div>
                        {needsToggle && (
                          <button className="wp-read-more-btn" onClick={() => toggleAccordion(akey)} aria-expanded={isExpanded}>
                            {isExpanded ? T.readLess : T.readMore}
                          </button>
                        )}
                      </div>
                    );
                  })}
                </div>

                <div ref={(el) => { detailSectionRefs.current.route = el; }} id="section-route"></div>
                <div className="wp-itinerary-wrap">
                  <div className="wp-itinerary-head">
                    <h3 className="wp-section-title" style={{ marginBottom: 0, display: "flex", alignItems: "center", gap: "0.5rem" }}><MapPinIcon size={18} style={{ color: continent.color }} /> {T.suggestedItinerary}</h3>
                    <span className="wp-itinerary-total">{country.itineraryDays} {country.itineraryDays === 1 ? T.day : T.days}</span>
                  </div>
                  {country.daysReason && <p className="wp-days-reason">{country.daysReason}</p>}

                  <button
                    className="wp-map-toggle-btn"
                    onClick={() => toggleAccordion("mapVisible:" + country.id)}
                    aria-expanded={!!openAccordion["mapVisible:" + country.id]}
                  >
                    <MapPinIcon size={15} />
                    {openAccordion["mapVisible:" + country.id] ? T.hideMap : T.showMap}
                  </button>
                  {openAccordion["mapVisible:" + country.id] && (
                    <CountryMap country={country} accentColor={continent.color} />
                  )}

                  <div className="wp-route">
                    {country.itinerary.map((step, i) => (
                      <div className="wp-day" style={{ "--accent-color": continent.color }} key={i}>
                        <span className="wp-day-label">{country.itinerary.some((s) => typeof s.lat === "number") ? (i + 1) + ". " : ""}{step.label}</span>
                        <div className="wp-day-title">{step.title}</div>
                        <div className="wp-day-desc">{step.desc}</div>
                        {(step.logistics || step.bookAhead) && (
                          <div className="wp-day-tags">
                            {step.logistics && <span className="wp-day-tag">{step.logistics}</span>}
                            {step.bookAhead && <span className="wp-day-tag wp-day-tag-book">{T.bookAhead}</span>}
                          </div>
                        )}
                        {step.cost && <div className="wp-day-extra"><strong>{T.cost}:</strong> {step.cost}</div>}
                        {step.food && <div className="wp-day-extra"><strong>{T.eat}:</strong> {step.food}</div>}
                      </div>
                    ))}
                  </div>
                </div>

                <div ref={(el) => { detailSectionRefs.current.faq = el; }} id="section-faq"></div>
                {country.faq && country.faq.length > 0 && (
                  <div className="wp-faq-wrap">
                    <h3 className="wp-section-title" style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}><ShieldCheck size={18} style={{ color: continent.color }} /> {T.faqTitle}</h3>
                    <div className="wp-accordion">
                      {country.faq.map((item, i) => {
                        const akey = "faq:" + country.id + ":" + i;
                        const isOpen = !!openAccordion[akey];
                        return (
                          <div className="wp-accordion-row" key={i}>
                            <button className="wp-accordion-trigger" onClick={() => toggleAccordion(akey)} aria-expanded={isOpen}>
                              <span className="wp-accordion-trigger-label wp-faq-q-label">{item.q}</span>
                              <ChevronRight size={15} className={"wp-accordion-chevron" + (isOpen ? " wp-accordion-chevron-open" : "")} />
                            </button>
                            {isOpen && <div className="wp-accordion-content">{item.a}</div>}
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}
              </>
            ) : countryDataCache["__error_" + country.id] ? (
              <div className="wp-detail-loading">
                <span>{T.countryDetailError}</span>
                <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ marginTop: "0.8rem" }} onClick={() => ensureCountryData(country.id)}>{T.tryAgain}</button>
              </div>
            ) : (
              <div className="wp-detail-loading"><span className="wp-map-loading-spinner"></span>{T.countryDetailLoading}</div>
            )}

            {country.pairsWith && country.pairsWith.length > 0 && (
              <div className="wp-pairs-wrap">
                <h3 className="wp-section-title">{T.pairsWith}</h3>
                <div className="wp-pairs-row">
                  {country.pairsWith.map((id) => {
                    const other = continents.flatMap((c) => c.countries).find((c) => c.id === id);
                    if (!other) return null;
                    return (
                      <button className="wp-pairs-card" key={id} onClick={() => goToCountryById(id)}>
                        <span>{other.flag}</span>
                        <span>{other.name}</span>
                        <ChevronRight size={16} style={{ color: "#8a8272" }} />
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        )}

        {view === "map" && (
          <div className="wp-map-page">
            <h2 className="wp-section-title" style={{ marginBottom: "0.2rem" }}>{T.mapTitle}</h2>
            <p className="wp-now-subtitle" style={{ marginBottom: "1.2rem" }}>{T.mapSubtitle}</p>

            {!user && (
              <div className="wp-map-signin-banner">
                <span>{T.mapSignInPrompt}</span>
                <button className="wp-signin-btn" style={{ marginLeft: 0 }} onClick={() => openAuthModal("signin")}>{T.signIn}</button>
              </div>
            )}

            {user && (
              <div className="wp-map-progress-row">
                <div className="wp-map-progress-stat">
                  <p className="wp-map-progress-value">{pctVisited}%</p>
                  <p className="wp-map-progress-label">{T.pctOfWorldVisited}</p>
                </div>
              </div>
            )}

            <div className="wp-map-legend">
              <span className="wp-map-legend-item"><span className="wp-status-dot wp-status-dot-visited"></span>{T.mapLegendVisited}</span>
              <span className="wp-map-legend-item"><span className="wp-status-dot wp-status-dot-want"></span>{T.mapLegendWant}</span>
              <span className="wp-map-legend-item"><span className="wp-status-dot wp-status-dot-none"></span>{T.mapLegendNone}</span>
            </div>

            <div className="wp-search-wrap" style={{ marginBottom: mapQuery.trim() ? "0" : "1.4rem" }}>
              <div className="wp-search-box">
                <Search size={16} className="wp-search-icon" />
                <input
                  type="text"
                  className="wp-search-input"
                  placeholder={T.searchHome}
                  value={mapQuery}
                  onChange={(e) => setMapQuery(e.target.value)}
                />
                {mapQuery && (
                  <button className="wp-search-clear" onClick={() => setMapQuery("")} aria-label="Clear search">
                    <X size={14} />
                  </button>
                )}
              </div>
            </div>
            {mapQuery.trim() && (
              <div className="wp-map-search-results">
                {mapSearchResults.length === 0 ? (
                  <p className="wp-search-empty">{T.noResultsFor} "{mapQuery}"</p>
                ) : (
                  mapSearchResults.map((cty) => (
                    <div key={cty.id} className="wp-map-search-row">
                      <div className="wp-map-search-row-info" onClick={() => goToDetailFromSearch(cty)}>
                        <div className="wp-country-name"><span>{cty.flag}</span>{cty.name}<StatusDot status={countryStatuses[cty.id]} /></div>
                        <div className="wp-country-capital">{cty.continentName}{cty.capital ? " · " + T.capital + ": " + cty.capital : ""}</div>
                      </div>
                      {firebaseReady && !authLoading && (
                        <div className="wp-status-row" title={!user ? T.signInToTrackHint : ""}>
                          <button
                            className={"wp-status-btn wp-status-visited" + (countryStatuses[cty.id] === "visited" ? " wp-status-active" : "")}
                            onClick={() => { setCountryStatus(cty.id, "visited"); setMapQuery(""); }}
                          >
                            <CheckCircle size={14} /> {T.markVisited}
                          </button>
                          <button
                            className={"wp-status-btn wp-status-want" + (countryStatuses[cty.id] === "want" ? " wp-status-active" : "")}
                            onClick={() => { setCountryStatus(cty.id, "want"); setMapQuery(""); }}
                          >
                            <StarIcon size={13} /> {T.markWantToVisit}
                          </button>
                        </div>
                      )}
                    </div>
                  ))
                )}
              </div>
            )}

            <div className="wp-map-frame wp-leaflet-frame">
              {!mapDataReady && !mapDataError && (
                <div className="wp-map-loading"><span className="wp-map-loading-spinner"></span>{T.mapLoading}</div>
              )}
              {mapDataError && (
                <div className="wp-map-loading">
                  <span>{T.mapLoadError}</span>
                  <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ marginTop: "0.6rem" }} onClick={retryMapData}>{T.tryAgain}</button>
                </div>
              )}
              <div ref={mapDivRef} className="wp-leaflet-map" style={{ visibility: mapDataReady ? "visible" : "hidden" }}></div>
              {mapDataReady && (
                <button
                  className="wp-map-reset-btn"
                  onClick={() => { if (leafletMapRef.current) leafletMapRef.current.setView([20, 12], 2); }}
                  aria-label="Reset view"
                >
                  <RefreshIcon size={14} />
                </button>
              )}
            </div>

            {popoverCountry && (
              <div className="wp-modal-overlay" onClick={() => setPopoverCountry(null)}>
                <div className="wp-map-popover" onClick={(e) => e.stopPropagation()}>
                  <button className="wp-modal-close" onClick={() => setPopoverCountry(null)} aria-label="Close"><X size={16} /></button>
                  <p className="wp-map-popover-name"><span>{popoverCountry.flag}</span>{popoverCountry.name}</p>
                  <p className="wp-map-popover-cont">{popoverCountry.continentName}</p>
                  {firebaseReady && !authLoading && (
                    <div className="wp-status-row" style={{ marginTop: "0.8rem" }}>
                      <button
                        className={"wp-status-btn wp-status-visited" + (countryStatuses[popoverCountry.id] === "visited" ? " wp-status-active" : "")}
                        onClick={() => setCountryStatus(popoverCountry.id, "visited")}
                      >
                        <CheckCircle size={14} /> {T.markVisited}
                      </button>
                      <button
                        className={"wp-status-btn wp-status-want" + (countryStatuses[popoverCountry.id] === "want" ? " wp-status-active" : "")}
                        onClick={() => setCountryStatus(popoverCountry.id, "want")}
                      >
                        <StarIcon size={13} /> {T.markWantToVisit}
                      </button>
                    </div>
                  )}
                </div>
              </div>
            )}

            <div className="wp-map-lists">
              <div className="wp-map-list-col">
                <h3 className="wp-map-list-title">{T.mapVisitedListTitle} <span className="wp-map-list-count">{mapVisitedCountries.length}</span></h3>
                {Object.keys(mapVisitedByContinent).length === 0 ? (
                  <p className="wp-map-list-empty">{T.mapListEmpty}</p>
                ) : (
                  Object.keys(mapVisitedByContinent).sort().map((contName) => (
                    <div key={contName} className="wp-map-list-group">
                      <div className="wp-map-list-continent">{contName}</div>
                      {mapVisitedByContinent[contName].map((cty) => (
                        <button key={cty.id} className="wp-map-list-row" onClick={() => goToDetailFromSearch(cty)}>
                          <span>{cty.flag}</span>{cty.name}
                        </button>
                      ))}
                    </div>
                  ))
                )}
              </div>
              <div className="wp-map-list-col">
                <h3 className="wp-map-list-title">{T.mapWantListTitle} <span className="wp-map-list-count">{mapWantCountries.length}</span></h3>
                {Object.keys(mapWantByContinent).length === 0 ? (
                  <p className="wp-map-list-empty">{T.mapListEmpty}</p>
                ) : (
                  Object.keys(mapWantByContinent).sort().map((contName) => (
                    <div key={contName} className="wp-map-list-group">
                      <div className="wp-map-list-continent">{contName}</div>
                      {mapWantByContinent[contName].map((cty) => (
                        <button key={cty.id} className="wp-map-list-row" onClick={() => goToDetailFromSearch(cty)}>
                          <span>{cty.flag}</span>{cty.name}
                        </button>
                      ))}
                    </div>
                  ))
                )}
              </div>
            </div>
          </div>
        )}

        {view === "trips" && (
          <div className="wp-trips-page">
            <h2 className="wp-section-title" style={{ marginBottom: "0.2rem" }}>{T.myTrips}</h2>
            <p className="wp-now-subtitle" style={{ marginBottom: "1.2rem" }}>{T.tripsSubtitle}</p>

            {!user && (
              <div className="wp-map-signin-banner">
                <span>{T.tripsSignInPrompt}</span>
                <button className="wp-signin-btn" style={{ marginLeft: 0 }} onClick={() => openAuthModal("signin")}>{T.signIn}</button>
              </div>
            )}

            {user && Object.keys(trips).length === 0 && (
              <p className="wp-map-list-empty" style={{ marginBottom: "1rem" }}>{T.noTripsYet}</p>
            )}

            {user && Object.keys(trips).length > 0 && (() => {
              const tripList = Object.values(trips);
              const continentIds = new Set();
              let totalNights = 0, totalDone = 0;
              tripList.forEach((trip) => {
                const tc = allCountriesFlat.find((c) => c.id === trip.countryId);
                if (tc) continentIds.add(tc.continentId);
                totalNights += Math.max(0, dayCount(trip.startDate, trip.endDate) - 1);
                if (trip.status === "done") totalDone += 1;
              });
              return (
                <div className="wp-trips-stat-strip">
                  <div className="wp-trips-stat-cell"><p className="wp-trips-stat-label">{T.tripsStatTrips}</p><p className="wp-trips-stat-value">{tripList.length}</p></div>
                  <div className="wp-trips-stat-cell"><p className="wp-trips-stat-label">{T.tripsStatContinents}</p><p className="wp-trips-stat-value">{continentIds.size}</p></div>
                  <div className="wp-trips-stat-cell"><p className="wp-trips-stat-label">{T.tripsStatNights}</p><p className="wp-trips-stat-value">{totalNights}</p></div>
                  <div className="wp-trips-stat-cell"><p className="wp-trips-stat-label">{T.tripsStatDone}</p><p className="wp-trips-stat-value">{totalDone}</p></div>
                </div>
              );
            })()}

            {user && Object.keys(trips).length > 0 && (
              <div className="wp-trips-grid">
                {Object.values(trips).map((trip) => {
                  const tc = allCountriesFlat.find((c) => c.id === trip.countryId);
                  const accent = (tc && tc.continentColor) || "#2F5D62";
                  return (
                    <button
                      key={trip.id}
                      className="wp-trip-card-v2"
                      onClick={() => { setActiveTripId(trip.id); setView("trip-detail"); window.scrollTo(0, 0); }}
                    >
                      <div className="wp-trip-card-v2-photo" style={{ background: "linear-gradient(135deg, " + accent + ", #142035)" }}>
                        <span className="wp-trip-card-v2-flag">{trip.flag}</span>
                        {tc && (
                          <span className="wp-trip-card-v2-icon"><ContinentIcon id={tc.continentId} size={16} /></span>
                        )}
                      </div>
                      <div className="wp-trip-card-v2-body">
                        <p className="wp-trip-card-v2-name">{trip.name}</p>
                        <p className="wp-trip-card-v2-meta">{dayCount(trip.startDate, trip.endDate)} {T.days} · {trip.stops.length} {T.stops}</p>
                        <span className={"wp-trip-card-v2-badge" + (trip.status === "done" ? " wp-trip-card-v2-badge-done" : "")}>
                          {trip.status === "done" ? T.tripStatusDone : T.tripStatusPlanning}
                        </span>
                      </div>
                    </button>
                  );
                })}
              </div>
            )}

            {user && (
              <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ marginTop: "1.3rem" }} onClick={openNewTripForm}>
                <PlusIcon size={15} /> {T.newTrip}
              </button>
            )}

            {showNewTripForm && (
              <div className="wp-modal-overlay" onClick={() => setShowNewTripForm(false)}>
                <div className="wp-auth-modal" onClick={(e) => e.stopPropagation()}>
                  <button className="wp-modal-close" onClick={() => setShowNewTripForm(false)} aria-label="Close"><X size={16} /></button>
                  <h2 className="wp-auth-title">{T.newTrip}</h2>

                  <label className="wp-field-label">{T.tripNameLabel}</label>
                  <input type="text" className="wp-auth-input" placeholder={T.tripNamePlaceholder} value={newTripName} onChange={(e) => setNewTripName(e.target.value)} />

                  <label className="wp-field-label">{T.tripCountryLabel}</label>
                  <input
                    type="text"
                    className="wp-auth-input"
                    placeholder={T.searchHome}
                    value={newTripCountryQuery}
                    onChange={(e) => { setNewTripCountryQuery(e.target.value); setNewTripCountryId(null); }}
                  />
                  {newTripCountryQuery.trim() && !newTripCountryId && (
                    <div className="wp-trip-country-results">
                      {allCountriesForMap.filter((c) => normalize(c.name).includes(normalize(newTripCountryQuery))).slice(0, 6).map((c) => (
                        <button key={c.id} className="wp-trip-country-row" onClick={() => { setNewTripCountryId(c.id); setNewTripCountryQuery(c.name); }}>
                          <span>{c.flag}</span>{c.name}
                        </button>
                      ))}
                    </div>
                  )}

                  <label className="wp-field-label">{T.tripDatesLabel}</label>
                  <div className="wp-trip-date-row">
                    <input type="date" className="wp-auth-input" value={newTripStart} onChange={(e) => setNewTripStart(e.target.value)} />
                    <input type="date" className="wp-auth-input" value={newTripEnd} onChange={(e) => setNewTripEnd(e.target.value)} />
                  </div>
                  {newTripStart && newTripEnd && (
                    <p className="wp-trip-days-hint">{dayCount(newTripStart, newTripEnd)} {T.daysWillBeCreated}</p>
                  )}

                  <button
                    className="wp-quiz-btn wp-quiz-btn-primary"
                    style={{ width: "100%", justifyContent: "center", marginTop: "0.6rem" }}
                    disabled={!newTripCountryId || !newTripName.trim()}
                    onClick={createTrip}
                  >
                    {T.createTrip}
                  </button>
                </div>
              </div>
            )}
          </div>
        )}

        {view === "trip-detail" && activeTripId && trips[activeTripId] && (() => {
          const trip = trips[activeTripId];
          const total = dayCount(trip.startDate, trip.endDate);
          const cost = tripTotalCost(trip);
          const countryData = withFullData(allCountriesFlat.find((c) => c.id === trip.countryId));
          const suggestions = countryData && countryData.attractions ? countryData.attractions.map((a) => a.name) : [];
          return (
            <div className="wp-trips-page">
              <div className="wp-trip-hero" style={{ "--trip-accent": (countryData && countryData.continentColor) || "#2F5D62" }}>
                <div className="wp-trip-hero-icon-bg">
                  {countryData ? <ContinentIcon id={countryData.continentId} size={220} /> : null}
                </div>
                <button className="wp-trip-hero-back" onClick={() => { setActiveTripId(null); goToStatic("trips"); }}>
                  <ChevronRight size={13} style={{ transform: "rotate(180deg)" }} /> {T.myTrips}
                </button>
                <div className="wp-trip-hero-row">
                  <div>
                    <div className="wp-trip-hero-title">
                      <span className="wp-trip-hero-flag">{trip.flag}</span>
                      <h1 className="wp-trip-hero-name">{trip.name}</h1>
                    </div>
                    <p className="wp-trip-hero-meta">{trip.startDate || "?"} – {trip.endDate || "?"} · {total} {T.days} · {trip.stops.length} {T.stops}</p>
                  </div>
                  <div className="wp-trip-hero-cost">
                    <p className="wp-trip-hero-cost-label">{T.estimatedCost}</p>
                    <p className="wp-trip-hero-cost-value">€{cost.toFixed(0)}</p>
                  </div>
                </div>
              </div>

              <div className="wp-trip-tabs">
                <div className="wp-trip-tab-row">
                  <button className={"wp-trip-tab" + (activeTripTab === "route" ? " wp-trip-tab-active" : "")} onClick={() => setActiveTripTab("route")}>{T.routeTab}</button>
                  <button className={"wp-trip-tab" + (activeTripTab === "days" ? " wp-trip-tab-active" : "")} onClick={() => setActiveTripTab("days")}>{T.daysTab}</button>
                  <button className={"wp-trip-tab" + (activeTripTab === "bookings" ? " wp-trip-tab-active" : "")} onClick={() => setActiveTripTab("bookings")}>{T.bookingsTab}</button>
                </div>
                <div className="wp-trip-header-actions">
                  <button className="wp-trip-header-btn" onClick={() => saveTripNow(trip.id)}>
                    <CheckCircle size={14} /> {tripSaveStatus === "saved" ? T.tripSaved : T.saveTrip}
                  </button>
                  <button className="wp-trip-header-btn" onClick={() => exportTripPDF(trip, countryData)}>
                    <Download size={14} /> {T.exportPdf}
                  </button>
                </div>
              </div>

              {activeTripTab === "route" && (
              <div className="wp-trip-route-layout">
              <div className="wp-trip-timeline-col">
              <div className="wp-trip-route-line"></div>

              {trip.stops.map((stop, i) => {
                const transit = trip.transits.find((tr) => tr.afterStopId === stop.id);
                const isActive = (type) => !!(activeEditPanel && activeEditPanel.stopId === stop.id && activeEditPanel.type === type);
                const transitEditing = isActive("transit");
                const sleepOpen = isActive("sleep");
                const eatOpen = isActive("eat");
                const highlightsOpen = isActive("highlights");
                return (
                <div key={stop.id}>
                  <button className="wp-trip-insert-link" onClick={() => insertStopBefore(trip.id, stop.id)}>
                    <PlusIcon size={11} /> {T.insertStopHere}
                  </button>

                  <div className="wp-trip-entry">
                    <span className={"wp-trip-entry-dot" + (stop.highlights.length || (stop.stays||[]).length || (stop.meals||[]).length ? " wp-trip-entry-dot-active" : "")}></span>
                    <div className="wp-trip-entry-photo" style={{ background: "linear-gradient(160deg, " + ((countryData && countryData.continentColor) || "#2F5D62") + ", #142035)" }}></div>
                    <div className="wp-trip-entry-body">
                      <div className="wp-trip-entry-head">
                        <input
                          type="text"
                          className="wp-trip-city-input"
                          placeholder={T.cityPlaceholder}
                          value={stop.city}
                          onChange={(e) => updateStopField(trip.id, stop.id, "city", e.target.value)}
                        />
                        <span className="wp-trip-entry-days">
                          {T.day}
                          <input
                            type="number" min="1" className="wp-trip-day-num"
                            value={stop.dayStart}
                            onChange={(e) => updateStopField(trip.id, stop.id, "dayStart", e.target.value === "" ? "" : parseInt(e.target.value))}
                            onBlur={(e) => { const n = parseInt(e.target.value); updateStopField(trip.id, stop.id, "dayStart", n > 0 ? n : 1); }}
                          />
                          -
                          <input
                            type="number" min="1" className="wp-trip-day-num"
                            value={stop.dayEnd}
                            onChange={(e) => updateStopField(trip.id, stop.id, "dayEnd", e.target.value === "" ? "" : parseInt(e.target.value))}
                            onBlur={(e) => { const n = parseInt(e.target.value); updateStopField(trip.id, stop.id, "dayEnd", n > 0 ? n : 1); }}
                          />
                        </span>
                        {trip.stops.length > 1 && (
                          <button className="wp-trip-remove-btn" onClick={() => removeStop(trip.id, stop.id)} aria-label="Remove stop"><X size={14} /></button>
                        )}
                      </div>
                      {formatDayRange(trip, stop.dayStart, stop.dayEnd) && (
                        <p className="wp-trip-date-range-hint">{formatDayRange(trip, stop.dayStart, stop.dayEnd)}</p>
                      )}

                      <div className="wp-trip-chips-row">
                        {stop.highlights.map((h) => (
                          <span key={h.id} className="wp-trip-chip">
                            {h.text}
                            <button className="wp-trip-chip-remove" onClick={() => removeHighlight(trip.id, stop.id, h.id)} aria-label="Remove"><X size={11} /></button>
                          </span>
                        ))}
                      </div>

                      <div className="wp-trip-panel-row">
                        <button
                          className={"wp-trip-panel-btn" + (highlightsOpen ? " wp-trip-panel-btn-active" : "") + (stop.highlights.length === 0 ? " wp-trip-panel-btn-empty" : "")}
                          onClick={(e) => openEditPanel(stop.id, "highlights", e.currentTarget)}
                        >
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={highlightsOpen ? "#2457E6" : "#586579"} strokeWidth="1.8"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
                          {T.placesBtn}
                        </button>
                        <button
                          className={"wp-trip-panel-btn" + (sleepOpen ? " wp-trip-panel-btn-active" : "") + ((stop.stays||[]).length === 0 ? " wp-trip-panel-btn-empty" : "")}
                          onClick={(e) => openEditPanel(stop.id, "sleep", e.currentTarget)}
                        >
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={sleepOpen ? "#2457E6" : "#586579"} strokeWidth="1.8"><path d="M3 18v-6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v6M3 18h18M3 18v2M21 18v2M5 10V7a2 2 0 0 1 2-2h3v5"/></svg>
                          {T.whereToSleepBtn}
                        </button>
                        <button
                          className={"wp-trip-panel-btn" + (eatOpen ? " wp-trip-panel-btn-active" : "") + ((stop.meals||[]).length === 0 ? " wp-trip-panel-btn-empty" : "")}
                          onClick={(e) => openEditPanel(stop.id, "eat", e.currentTarget)}
                        >
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={eatOpen ? "#2457E6" : "#586579"} strokeWidth="1.8"><path d="M6 3v7a3 3 0 0 0 6 0V3M9 10v11M18 3c-1.5 2-1.5 5 0 7v11"/></svg>
                          {T.whereToEatBtn}
                        </button>
                      </div>

                      {(stop.stays || []).length > 0 && (
                        <button className="wp-trip-summary-line" onClick={(e) => openEditPanel(stop.id, "sleep", e.currentTarget)}>
                          🛏 {stop.stays[0].name}{stop.stays[0].nights ? " · " + stop.stays[0].nights + " " + T.nights : ""}{stop.stays.length > 1 ? " · +" + (stop.stays.length - 1) + " " + T.placesCountSuffix : ""}
                        </button>
                      )}
                      {(stop.meals || []).length > 0 && (
                        <button className="wp-trip-summary-line" onClick={(e) => openEditPanel(stop.id, "eat", e.currentTarget)}>
                          🍽 {stop.meals[0].name}{stop.meals.length > 1 ? " · +" + (stop.meals.length - 1) + " " + T.placesCountSuffix : ""}
                        </button>
                      )}
                    </div>
                  </div>

                  {i < trip.stops.length - 1 && transit && (
                    <div className="wp-trip-transit-summary-row" onClick={(e) => openEditPanel(stop.id, "transit", e.currentTarget)} onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openEditPanel(stop.id, "transit", e.currentTarget); } }} role="button" tabIndex={0}>
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FF8A3D" strokeWidth="1.8"><path d="M4 16h16M4 16l3-3M4 16l3 3M20 16a2 2 0 1 0-4 0"/></svg>
                      <span className="wp-trip-transit-summary-text">
                        {transit.mode
                          ? (transit.durationHours || transit.durationMinutes ? (transit.durationHours || "0") + "h" + (transit.durationMinutes ? transit.durationMinutes + "min" : "") + " · " : "") + (T["transit" + transit.mode.charAt(0).toUpperCase() + transit.mode.slice(1)] || transit.mode)
                          : T.transitAddBtn}
                      </span>
                      <span className="wp-trip-transit-summary-edit">{transit.mode ? T.transitEditBtn : T.transitAddBtn}</span>
                    </div>
                  )}
                  {i < trip.stops.length - 1 && transit && transit.mode && (
                    <p className="wp-trip-typical-hint">{T.typicalRange}: {TRANSIT_TYPICAL[transit.mode]}</p>
                  )}
                </div>
              );})}

              {activeEditPanel && (() => {
                const aStop = trip.stops.find((s) => s.id === activeEditPanel.stopId);
                if (!aStop) return null;
                const aTransit = trip.transits.find((tr) => tr.afterStopId === activeEditPanel.stopId);
                const titleMap = { highlights: T.placesBtn, sleep: T.whereToSleep, eat: T.whereToEat, transit: T.transportTitle };
                return (
                  <div className="wp-task-sheet-overlay" onClick={closeEditPanel}>
                    <div
                      className="wp-task-sheet-panel"
                      ref={editPanelRef}
                      role="dialog"
                      aria-modal="true"
                      aria-label={titleMap[activeEditPanel.type]}
                      onClick={(e) => e.stopPropagation()}
                    >
                      <div className="wp-task-sheet-head">
                        <div>
                          <p className="wp-task-sheet-title">{titleMap[activeEditPanel.type]}</p>
                          <p className="wp-task-sheet-context">{aStop.city || T.cityPlaceholder}</p>
                        </div>
                        <button className="wp-mobile-menu-close" onClick={closeEditPanel} aria-label={T.closeMenu}><X size={18} /></button>
                      </div>

                      <div className="wp-task-sheet-scroll">
                        {activeEditPanel.type === "highlights" && (
                          <>
                            {aStop.highlights.length > 0 && (
                              <div className="wp-trip-chips-row" style={{ marginBottom: "1rem" }}>
                                {aStop.highlights.map((h) => (
                                  <span key={h.id} className="wp-trip-chip">
                                    {h.text}
                                    <button className="wp-trip-chip-remove" onClick={() => removeHighlight(trip.id, aStop.id, h.id)} aria-label="Remove"><X size={11} /></button>
                                  </span>
                                ))}
                              </div>
                            )}
                            <div className="wp-trip-add-highlight-row">
                              <input
                                type="text"
                                className="wp-trip-highlight-input"
                                placeholder={T.addHighlightPlaceholder}
                                value={highlightDrafts[aStop.id] || ""}
                                onChange={(e) => setHighlightDrafts({ ...highlightDrafts, [aStop.id]: e.target.value })}
                                onKeyDown={(e) => {
                                  if (e.key === "Enter" && (highlightDrafts[aStop.id] || "").trim()) {
                                    addHighlight(trip.id, aStop.id, highlightDrafts[aStop.id], "custom");
                                    setHighlightDrafts({ ...highlightDrafts, [aStop.id]: "" });
                                  }
                                }}
                              />
                              <button
                                className="wp-trip-add-btn"
                                onClick={() => {
                                  if ((highlightDrafts[aStop.id] || "").trim()) {
                                    addHighlight(trip.id, aStop.id, highlightDrafts[aStop.id], "custom");
                                    setHighlightDrafts({ ...highlightDrafts, [aStop.id]: "" });
                                  }
                                }}
                              ><PlusIcon size={14} /></button>
                            </div>
                            {suggestions.length > 0 && (
                              <>
                                <p className="wp-trip-suggestions-label">{T.suggestionsIn} {countryData ? countryData.name : (trip.countryName || "")}</p>
                                <div className="wp-trip-suggestions">
                                  {suggestions.filter((s) => !aStop.highlights.some((h) => h.text === s)).slice(0, 4).map((s) => (
                                    <button key={s} className="wp-trip-suggestion-chip" onClick={() => addHighlight(trip.id, aStop.id, s, "attraction")}>
                                      <PlusIcon size={11} /> {s}
                                    </button>
                                  ))}
                                </div>
                              </>
                            )}
                          </>
                        )}

                        {activeEditPanel.type === "sleep" && (
                          <>
                            {(aStop.stays || []).map((st) => (
                              <div key={st.id} className="wp-trip-highlight-row">
                                <span style={{ fontSize: "0.85rem" }}>🏨</span>
                                <span className="wp-trip-highlight-text">{st.name}{st.nights ? " · " + st.nights + " " + T.nights : ""}{st.price ? " · " + st.price : ""}</span>
                                <button className="wp-trip-remove-btn" onClick={() => removeStay(trip.id, aStop.id, st.id)} aria-label="Remove"><X size={12} /></button>
                              </div>
                            ))}
                            <div className="wp-trip-add-highlight-row">
                              <input type="text" className="wp-trip-highlight-input" style={{ flex: 2 }} placeholder={T.stayNamePlaceholder}
                                value={(stayDrafts[aStop.id] || {}).name || ""}
                                onChange={(e) => setStayDrafts({ ...stayDrafts, [aStop.id]: { ...(stayDrafts[aStop.id] || {}), name: e.target.value } })} />
                              <input type="text" className="wp-trip-highlight-input" style={{ flex: 1 }} placeholder={T.nightsPlaceholder}
                                value={(stayDrafts[aStop.id] || {}).nights || ""}
                                onChange={(e) => setStayDrafts({ ...stayDrafts, [aStop.id]: { ...(stayDrafts[aStop.id] || {}), nights: e.target.value } })} />
                              <input type="text" className="wp-trip-highlight-input" style={{ flex: 1 }} placeholder={T.transitPrice}
                                value={(stayDrafts[aStop.id] || {}).price || ""}
                                onChange={(e) => setStayDrafts({ ...stayDrafts, [aStop.id]: { ...(stayDrafts[aStop.id] || {}), price: e.target.value } })} />
                              <button className="wp-trip-add-btn" onClick={() => {
                                const d = stayDrafts[aStop.id] || {};
                                addStay(trip.id, aStop.id, d.name || "", d.nights || "", d.price || "");
                                setStayDrafts({ ...stayDrafts, [aStop.id]: {} });
                              }}><PlusIcon size={14} /></button>
                            </div>
                          </>
                        )}

                        {activeEditPanel.type === "eat" && (
                          <>
                            {(aStop.meals || []).map((m) => (
                              <div key={m.id} className="wp-trip-highlight-row">
                                <span style={{ fontSize: "0.85rem" }}>🍽</span>
                                <span className="wp-trip-highlight-text">{m.name}</span>
                                <button className="wp-trip-remove-btn" onClick={() => removeMeal(trip.id, aStop.id, m.id)} aria-label="Remove"><X size={12} /></button>
                              </div>
                            ))}
                            <div className="wp-trip-add-highlight-row">
                              <input type="text" className="wp-trip-highlight-input" placeholder={T.addMealPlaceholder}
                                value={(mealDrafts[aStop.id] || {}).name || ""}
                                onChange={(e) => setMealDrafts({ ...mealDrafts, [aStop.id]: { ...(mealDrafts[aStop.id] || {}), name: e.target.value } })}
                                onKeyDown={(e) => {
                                  if (e.key === "Enter" && ((mealDrafts[aStop.id] || {}).name || "").trim()) {
                                    addMeal(trip.id, aStop.id, mealDrafts[aStop.id].name);
                                    setMealDrafts({ ...mealDrafts, [aStop.id]: {} });
                                  }
                                }} />
                              <button className="wp-trip-add-btn" onClick={() => {
                                const d = mealDrafts[aStop.id] || {};
                                addMeal(trip.id, aStop.id, d.name || "");
                                setMealDrafts({ ...mealDrafts, [aStop.id]: {} });
                              }}><PlusIcon size={14} /></button>
                            </div>
                            {countryData && countryData.food && countryData.food.length > 0 && (
                              <>
                                <p className="wp-trip-suggestions-label">{T.suggestionsIn} {countryData.name}</p>
                                <div className="wp-trip-suggestions">
                                  {countryData.food.filter((f) => !aStop.meals.some((m) => m.name === f.name)).slice(0, 3).map((f) => (
                                    <button key={f.name} className="wp-trip-suggestion-chip" onClick={() => addMeal(trip.id, aStop.id, f.name)}>
                                      <PlusIcon size={11} /> {f.name}
                                    </button>
                                  ))}
                                </div>
                              </>
                            )}
                          </>
                        )}

                        {activeEditPanel.type === "transit" && aTransit && (
                          <div className="wp-trip-transit-edit-form">
                            <div className="wp-trip-field-group">
                              <label className="wp-trip-field-label">{T.transportModeLabel}</label>
                              <select
                                className="wp-trip-transit-select"
                                value={aTransit.mode}
                                onChange={(e) => updateTransit(trip.id, aStop.id, "mode", e.target.value)}
                              >
                                <option value="">{T.chooseTransit}</option>
                                <option value="flight">{T.transitFlight}</option>
                                <option value="train">{T.transitTrain}</option>
                                <option value="bus">{T.transitBus}</option>
                                <option value="car">{T.transitCar}</option>
                                <option value="boat">{T.transitBoat}</option>
                              </select>
                            </div>
                            <div className="wp-trip-field-group">
                              <label className="wp-trip-field-label">{T.transportDurationLabel}</label>
                              <div className="wp-trip-transit-duration-row">
                                <input
                                  type="number" min="0" className="wp-trip-transit-input wp-trip-transit-num"
                                  placeholder={T.hoursLabel}
                                  value={aTransit.durationHours}
                                  onChange={(e) => updateTransit(trip.id, aStop.id, "durationHours", e.target.value)}
                                />
                                <input
                                  type="number" min="0" max="59" className="wp-trip-transit-input wp-trip-transit-num"
                                  placeholder={T.minutesLabel}
                                  value={aTransit.durationMinutes}
                                  onChange={(e) => updateTransit(trip.id, aStop.id, "durationMinutes", e.target.value)}
                                />
                              </div>
                            </div>
                            <div className="wp-trip-field-group">
                              <label className="wp-trip-field-label">{T.transportCostLabel}</label>
                              <input
                                type="text" className="wp-trip-transit-input"
                                placeholder={T.transitPrice}
                                value={aTransit.price}
                                onChange={(e) => updateTransit(trip.id, aStop.id, "price", e.target.value)}
                              />
                            </div>
                            {aTransit.mode && (
                              <p className="wp-trip-typical-hint">{T.typicalRange}: {TRANSIT_TYPICAL[aTransit.mode]}</p>
                            )}
                          </div>
                        )}
                      </div>

                      <div className="wp-task-sheet-footer">
                        <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ width: "100%", justifyContent: "center" }} onClick={closeEditPanel}>{T.doneEditingLabel}</button>
                      </div>
                    </div>
                  </div>
                );
              })()}

              <button className="wp-trip-add-stop-btn" onClick={() => addStop(trip.id)}>
                <PlusIcon size={15} /> {T.addStop}
              </button>

              </div>
              <TripMap trip={trip} countryName={countryData ? countryData.name : (trip.countryName || "")} geocodeCache={geocodeCache} geocodeCity={geocodeCity} accentColor={(countryData && countryData.continentColor) || "#2F5D62"} T={T} />
              </div>
              )}

              {activeTripTab === "days" && (() => {
                const dayStop = stopForDay(trip, selectedDay);
                const dayActivities = (trip.days && trip.days[selectedDay]) || [];
                const dayDate = trip.startDate ? new Date(new Date(trip.startDate).getTime() + (selectedDay - 1) * 86400000) : null;
                const draft = activityDrafts[selectedDay] || {};
                return (
                  <div className="wp-trip-days-tab">
                    <div className="wp-trip-day-pills">
                      {Array.from({ length: total }, (_, i) => i + 1).map((d) => {
                        const dt = trip.startDate ? new Date(new Date(trip.startDate).getTime() + (d - 1) * 86400000) : null;
                        return (
                          <button
                            key={d}
                            className={"wp-trip-day-pill" + (selectedDay === d ? " wp-trip-day-pill-active" : "")}
                            onClick={() => setSelectedDay(d)}
                          >
                            {dt ? dt.toLocaleDateString(lang === "pt" ? "pt-PT" : "en-GB", { day: "numeric", month: "short" }) : T.day + " " + d}
                          </button>
                        );
                      })}
                    </div>

                    <div className="wp-trip-day-header-row">
                      <p className="wp-trip-day-city">{dayStop ? dayStop.city || T.cityPlaceholder : ""}</p>
                      <div className="wp-trip-day-view-toggle">
                        <button className={"wp-trip-day-view-btn" + (dayView === "list" ? " wp-trip-day-view-btn-active" : "")} onClick={() => setDayView("list")}>{T.listViewLabel}</button>
                        <button className={"wp-trip-day-view-btn" + (dayView === "map" ? " wp-trip-day-view-btn-active" : "")} onClick={() => setDayView("map")}>{T.mapViewLabel}</button>
                      </div>
                    </div>

                    {dayStop && dayStop.highlights.filter((h) => !dayActivities.some((a) => a.name === h.text)).length > 0 && (
                      <div className="wp-trip-day-suggestions">
                        <p className="wp-trip-day-suggestions-label">{T.daySuggestionsLabel}</p>
                        <div className="wp-trip-chips-row">
                          {dayStop.highlights.filter((h) => !dayActivities.some((a) => a.name === h.text)).map((h) => (
                            <button key={h.id} className="wp-trip-suggestion-chip" onClick={() => addDayActivity(trip.id, selectedDay, "", h.text)}>
                              <PlusIcon size={11} /> {h.text}
                            </button>
                          ))}
                        </div>
                      </div>
                    )}

                    {dayView === "list" ? (
                      <div className="wp-trip-day-list">
                        {dayActivities.length === 0 && <p className="wp-trip-day-list-empty">{T.dayListEmpty}</p>}
                        {dayActivities.map((a) => (
                          <div key={a.id} className="wp-trip-day-activity-row">
                            {a.time && <span className="wp-trip-day-activity-time">{a.time}</span>}
                            <span className="wp-trip-day-activity-name">{a.name}</span>
                            <button className="wp-trip-remove-btn" onClick={() => removeDayActivity(trip.id, selectedDay, a.id)} aria-label="Remove"><X size={12} /></button>
                          </div>
                        ))}
                        <div className="wp-trip-add-highlight-row" style={{ marginTop: "0.7rem" }}>
                          <input
                            type="text"
                            className="wp-trip-highlight-input"
                            style={{ flex: "0 0 90px" }}
                            placeholder={T.activityTimePlaceholder}
                            value={draft.time || ""}
                            onChange={(e) => setActivityDrafts({ ...activityDrafts, [selectedDay]: { ...draft, time: e.target.value } })}
                          />
                          <input
                            type="text"
                            className="wp-trip-highlight-input"
                            placeholder={T.addActivityPlaceholder}
                            value={draft.name || ""}
                            onChange={(e) => setActivityDrafts({ ...activityDrafts, [selectedDay]: { ...draft, name: e.target.value } })}
                            onKeyDown={(e) => {
                              if (e.key === "Enter" && (draft.name || "").trim()) {
                                addDayActivity(trip.id, selectedDay, draft.time, draft.name);
                                setActivityDrafts({ ...activityDrafts, [selectedDay]: { time: "", name: "" } });
                              }
                            }}
                          />
                          <button
                            className="wp-trip-add-btn"
                            onClick={() => {
                              if ((draft.name || "").trim()) {
                                addDayActivity(trip.id, selectedDay, draft.time, draft.name);
                                setActivityDrafts({ ...activityDrafts, [selectedDay]: { time: "", name: "" } });
                              }
                            }}
                          ><PlusIcon size={14} /></button>
                        </div>
                      </div>
                    ) : (
                      <DayMap
                        activities={dayActivities}
                        cityName={dayStop ? dayStop.city : ""}
                        countryName={countryData ? countryData.name : (trip.countryName || "")}
                        geocodeCache={geocodeCache}
                        geocodeCity={geocodeCity}
                        accentColor={(countryData && countryData.continentColor) || "#2F5D62"}
                        T={T}
                      />
                    )}
                  </div>
                );
              })()}

              {activeTripTab === "bookings" && (
                <div className="wp-trip-bookings-tab">
                  <div className="wp-trip-day-view-toggle" style={{ marginBottom: "1.3rem" }}>
                    <button className={"wp-trip-day-view-btn" + (bookingsSubTab === "all" ? " wp-trip-day-view-btn-active" : "")} onClick={() => setBookingsSubTab("all")}>{T.bookingsAll}</button>
                    <button className={"wp-trip-day-view-btn" + (bookingsSubTab === "flights" ? " wp-trip-day-view-btn-active" : "")} onClick={() => setBookingsSubTab("flights")}>{T.bookingsFlights}</button>
                    <button className={"wp-trip-day-view-btn" + (bookingsSubTab === "hotels" ? " wp-trip-day-view-btn-active" : "")} onClick={() => setBookingsSubTab("hotels")}>{T.bookingsHotels}</button>
                  </div>

                  {(bookingsSubTab === "all" || bookingsSubTab === "flights") && (() => {
                    const flightTransits = trip.transits.filter((tr) => tr.mode === "flight");
                    return (
                      <div className="wp-trip-booking-section">
                        <p className="wp-trip-booking-section-title">✈️ {T.bookingsFlights}</p>
                        {flightTransits.length === 0 && <p className="wp-trip-day-list-empty">{T.noFlightsYet}</p>}
                        {flightTransits.map((tr) => {
                          const fromStop = trip.stops.find((s) => s.id === tr.afterStopId);
                          const fromIdx = trip.stops.findIndex((s) => s.id === tr.afterStopId);
                          const toStop = trip.stops[fromIdx + 1];
                          return (
                            <div key={tr.afterStopId} className="wp-trip-booking-card">
                              <div className="wp-trip-booking-card-head">
                                <span className="wp-trip-booking-route">{fromStop ? fromStop.city : "?"} → {toStop ? toStop.city : "?"}</span>
                                <button
                                  className={"wp-trip-confirm-toggle" + (tr.confirmed ? " wp-trip-confirm-toggle-on" : "")}
                                  onClick={() => toggleTransitConfirmed(trip.id, tr.afterStopId)}
                                >
                                  {tr.confirmed ? T.confirmedLabel : T.pendingLabel}
                                </button>
                              </div>
                              <div className="wp-trip-add-highlight-row">
                                <input type="text" className="wp-trip-highlight-input" placeholder={T.flightNumberPlaceholder}
                                  value={tr.flightNumber || ""} onChange={(e) => updateTransit(trip.id, tr.afterStopId, "flightNumber", e.target.value)} />
                                <input type="text" className="wp-trip-highlight-input" placeholder={T.flightTimePlaceholder}
                                  value={tr.flightTime || ""} onChange={(e) => updateTransit(trip.id, tr.afterStopId, "flightTime", e.target.value)} />
                                <input type="text" className="wp-trip-highlight-input" placeholder={T.flightRefPlaceholder}
                                  value={tr.reference || ""} onChange={(e) => updateTransit(trip.id, tr.afterStopId, "reference", e.target.value)} />
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    );
                  })()}

                  {(bookingsSubTab === "all" || bookingsSubTab === "hotels") && (() => {
                    const stopsWithStays = trip.stops.filter((s) => (s.stays || []).length > 0);
                    return (
                      <div className="wp-trip-booking-section">
                        <p className="wp-trip-booking-section-title">🛏 {T.bookingsHotels}</p>
                        {stopsWithStays.length === 0 && <p className="wp-trip-day-list-empty">{T.noHotelsYet}</p>}
                        {stopsWithStays.map((s) => s.stays.map((st) => (
                          <div key={st.id} className="wp-trip-booking-card">
                            <div className="wp-trip-booking-card-head">
                              <span className="wp-trip-booking-route">{st.name} · {s.city}{st.nights ? " · " + st.nights + " " + T.nights : ""}{st.price ? " · " + st.price : ""}</span>
                              <button
                                className={"wp-trip-confirm-toggle" + (st.confirmed ? " wp-trip-confirm-toggle-on" : "")}
                                onClick={() => toggleStayConfirmed(trip.id, s.id, st.id)}
                              >
                                {st.confirmed ? T.confirmedLabel : T.pendingLabel}
                              </button>
                            </div>
                          </div>
                        )))}
                      </div>
                    );
                  })()}

                  <div className="wp-trip-booking-section">
                    <p className="wp-trip-booking-section-title">📄 {T.documentsTitle}</p>
                    {(trip.documents || []).length === 0 && <p className="wp-trip-day-list-empty">{T.noDocumentsYet}</p>}
                    {(trip.documents || []).map((d) => (
                      <div key={d.id} className="wp-trip-day-activity-row">
                        <span className="wp-trip-day-activity-name">{d.text}</span>
                        <button className="wp-trip-remove-btn" onClick={() => removeDocument(trip.id, d.id)} aria-label="Remove"><X size={12} /></button>
                      </div>
                    ))}
                    <div className="wp-trip-add-highlight-row" style={{ marginTop: "0.7rem" }}>
                      <input
                        type="text"
                        className="wp-trip-highlight-input"
                        placeholder={T.addDocumentPlaceholder}
                        value={documentDraft}
                        onChange={(e) => setDocumentDraft(e.target.value)}
                        onKeyDown={(e) => { if (e.key === "Enter" && documentDraft.trim()) { addDocument(trip.id, documentDraft); setDocumentDraft(""); } }}
                      />
                      <button className="wp-trip-add-btn" onClick={() => { if (documentDraft.trim()) { addDocument(trip.id, documentDraft); setDocumentDraft(""); } }}><PlusIcon size={14} /></button>
                    </div>
                  </div>

                  <button className="wp-trip-view-in-route-link" onClick={() => setActiveTripTab("route")}>{T.viewInRoute} →</button>
                </div>
              )}

              <div className="wp-trip-share-box">
                <div className="wp-trip-share-row">
                  <div>
                    <p className="wp-trip-share-title">{T.shareTrip}</p>
                    <p className="wp-trip-share-desc">{trip.isPublic ? T.shareTripOnDesc : T.shareTripOffDesc}</p>
                  </div>
                  <button
                    className={"wp-trip-share-toggle" + (trip.isPublic ? " wp-trip-share-toggle-on" : "")}
                    onClick={() => toggleTripPublic(trip)}
                    aria-pressed={!!trip.isPublic}
                    aria-label={T.shareTrip}
                  >
                    <span className="wp-trip-share-toggle-knob"></span>
                  </button>
                </div>
                {trip.isPublic && trip.shareId && (
                  <div className="wp-trip-share-link-row">
                    <input
                      type="text"
                      readOnly
                      className="wp-trip-share-link-input"
                      value={window.location.origin + window.location.pathname + "#shared=" + trip.shareId}
                      onFocus={(e) => e.target.select()}
                    />
                    <button className="wp-trip-add-btn" onClick={() => copyShareLink(trip.shareId)} aria-label={T.copyLink}>
                      {shareCopied ? <CheckCircle size={14} /> : <Copy size={14} />}
                    </button>
                  </div>
                )}
              </div>

              <div className="wp-trip-notes-box">
                <p className="wp-trip-notes-title">{T.dayNotes}</p>
                <p className="wp-trip-notes-subtitle">{T.dayNotesSubtitle}</p>
                <div className="wp-trip-timeline">
                  <div className="wp-trip-timeline-line"></div>
                  {Array.from({ length: total }, (_, i) => i + 1).map((day) => {
                    const covering = trip.stops.find((s) => day >= s.dayStart && day <= s.dayEnd);
                    const noteText = (trip.dailyNotes || {})[day] || "";
                    const isEditing = editingNoteDay === day;
                    return (
                      <div key={day} className="wp-trip-timeline-entry">
                        <span className={"wp-trip-timeline-dot" + (noteText.trim() ? " wp-trip-timeline-dot-filled" : "")}></span>
                        <p className="wp-trip-timeline-day">
                          <b>{T.day} {day}</b>
                          {covering && covering.city ? <span className="wp-trip-timeline-city"> · {covering.city}</span> : null}
                        </p>
                        {isEditing ? (
                          <textarea
                            autoFocus
                            className="wp-trip-timeline-input"
                            rows={2}
                            placeholder={T.dayNotesPlaceholder}
                            value={noteText}
                            onChange={(e) => updateDailyNote(trip.id, day, e.target.value)}
                            onBlur={() => setEditingNoteDay(null)}
                          />
                        ) : noteText.trim() ? (
                          <p className="wp-trip-timeline-note" onClick={() => setEditingNoteDay(day)}>{noteText}</p>
                        ) : (
                          <button className="wp-trip-timeline-add" onClick={() => setEditingNoteDay(day)}>{T.addNoteForDay}</button>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>

              <div className="wp-trip-footer-actions">
                {trip.status !== "done" && (
                  <button className="wp-quiz-btn wp-quiz-btn-primary" onClick={() => markTripDone(trip.id)}>{T.markTripDone}</button>
                )}
                <button className="wp-trip-delete-btn" onClick={() => { if (window.confirm(T.confirmDeleteTrip)) deleteTrip(trip.id); }}>{T.deleteTrip}</button>
              </div>
            </div>
          );
        })()}

        {view === "shared-trip" && (
          <div className="wp-trips-page">
            <a className="wp-trip-back" href="index.html">
              <ChevronRight size={15} style={{ transform: "rotate(180deg)" }} /> {T.backToWaypoint}
            </a>

            <div className="wp-shared-trip-banner">{T.sharedTripBanner}</div>

            {sharedTripStatus === "loading" && <p className="wp-map-list-empty">{T.sharedTripLoading}</p>}
            {sharedTripStatus === "error" && <p className="wp-map-list-empty">{T.sharedTripNotFound}</p>}

            {sharedTripStatus === "ready" && sharedTrip && (() => {
              const total = dayCount(sharedTrip.startDate, sharedTrip.endDate);
              const cost = tripTotalCost(sharedTrip);
              const stops = sharedTrip.stops || [];
              const transits = sharedTrip.transits || [];
              const notes = sharedTrip.dailyNotes || {};
              return (
                <React.Fragment>
                  <div className="wp-trip-detail-header">
                    <div className="wp-trip-card-top">
                      <span className="wp-trip-card-name"><span>{sharedTrip.flag}</span>{sharedTrip.name}</span>
                    </div>
                    <p className="wp-trip-card-meta">{sharedTrip.startDate || "?"} – {sharedTrip.endDate || "?"} · {total} {T.days} · {stops.length} {T.stops}</p>
                  </div>

                  <div className="wp-trip-cost-row">
                    <div className="wp-trip-cost-box">
                      <p className="wp-trip-cost-label">{T.estimatedCost}</p>
                      <p className="wp-trip-cost-value">€{cost.toFixed(0)}</p>
                    </div>
                    <div className="wp-trip-cost-box">
                      <p className="wp-trip-cost-label">{T.perDay}</p>
                      <p className="wp-trip-cost-value">€{(cost / total).toFixed(0)}</p>
                    </div>
                  </div>

                  {stops.map((stop, i) => {
                    const transit = transits.find((tr) => tr.afterStopId === stop.id);
                    return (
                      <div key={stop.id || i}>
                        <div className="wp-trip-stop-card">
                          <div className="wp-trip-stop-top">
                            <span className="wp-trip-city-readonly">{stop.city || "—"}</span>
                            <span className="wp-trip-day-range-edit">{T.day} {stop.dayStart}–{stop.dayEnd}</span>
                          </div>

                          {(stop.highlights || []).map((h) => (
                            <div key={h.id} className="wp-trip-highlight-row">
                              <CheckCircle size={14} style={{ color: "#6B9E68", flexShrink: 0 }} />
                              <span className="wp-trip-highlight-text">{h.text}</span>
                            </div>
                          ))}

                          {(stop.stays || []).length > 0 && (
                            <div className="wp-trip-subsection">
                              <p className="wp-trip-subsection-label">{T.whereToSleep}</p>
                              {stop.stays.map((st) => (
                                <div key={st.id} className="wp-trip-highlight-row">
                                  <span style={{ fontSize: "0.85rem" }}>🏨</span>
                                  <span className="wp-trip-highlight-text">{st.name}{st.nights ? " · " + st.nights + " " + T.nights : ""}{st.price ? " · " + st.price : ""}</span>
                                </div>
                              ))}
                            </div>
                          )}

                          {(stop.meals || []).length > 0 && (
                            <div className="wp-trip-subsection">
                              <p className="wp-trip-subsection-label">{T.whereToEat}</p>
                              {stop.meals.map((m) => (
                                <div key={m.id} className="wp-trip-highlight-row">
                                  <span style={{ fontSize: "0.85rem" }}>🍽</span>
                                  <span className="wp-trip-highlight-text">{m.name}</span>
                                </div>
                              ))}
                            </div>
                          )}
                        </div>

                        {i < stops.length - 1 && transit && transit.mode && (
                          <p className="wp-trip-typical-hint" style={{ marginLeft: "1.2rem" }}>
                            {T["transit" + transit.mode.charAt(0).toUpperCase() + transit.mode.slice(1)]}
                            {transit.durationHours ? " · " + transit.durationHours + "h" : ""}{transit.durationMinutes ? transit.durationMinutes + "min" : ""}
                            {transit.price ? " · " + transit.price : ""}
                          </p>
                        )}
                      </div>
                    );
                  })}

                  {Object.keys(notes).some((d) => (notes[d] || "").trim()) && (
                    <div className="wp-trip-notes-box">
                      <p className="wp-trip-notes-title">{T.dayNotes}</p>
                      <p className="wp-trip-notes-subtitle">{T.dayNotesSubtitle}</p>
                      <div className="wp-trip-timeline">
                        <div className="wp-trip-timeline-line"></div>
                        {Array.from({ length: total }, (_, i) => i + 1).map((day) => {
                          const covering = stops.find((s) => day >= s.dayStart && day <= s.dayEnd);
                          const noteText = notes[day] || "";
                          return (
                            <div key={day} className="wp-trip-timeline-entry">
                              <span className={"wp-trip-timeline-dot" + (noteText.trim() ? " wp-trip-timeline-dot-filled" : "")}></span>
                              <p className="wp-trip-timeline-day"><b>{T.day} {day}</b>{covering && covering.city ? <span className="wp-trip-timeline-city"> · {covering.city}</span> : null}</p>
                              {noteText.trim() && <p className="wp-trip-timeline-note wp-trip-timeline-note-readonly">{noteText}</p>}
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  )}

                  <a className="wp-quiz-btn wp-quiz-btn-primary" href="index.html" style={{ display: "inline-flex", textDecoration: "none", marginTop: "1rem" }}>
                    {T.planYourOwnTrip}
                  </a>
                </React.Fragment>
              );
            })()}
          </div>
        )}

        {view === "articles" && (
          <div>
            <h2 className="wp-section-title" style={{ marginBottom: "1.3rem" }}>{T.articles}</h2>
            <a href="articles/namibia-solo-road-trip.html" style={{ display: "block", background: "#fff", border: "1px solid var(--hairline)", borderRadius: "10px", padding: "1.3rem 1.4rem", textDecoration: "none", color: "var(--ink)", marginBottom: "1rem" }}>
              <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", fontSize: "0.85rem", color: "var(--gold)", fontWeight: 600, marginBottom: "0.6rem" }}><span style={{ width: 6, height: 6, borderRadius: "50%", background: "var(--gold)", display: "inline-block" }}></span>Trip report · Namibia</div>
              <div style={{ fontSize: "1.25rem", fontWeight: 600, marginBottom: "0.5rem" }}>Ten Days of Silence: A Solo Self-Drive Through Namibia</div>
              <div style={{ fontSize: "0.92rem", color: "#4a4436", lineHeight: 1.55 }}>A practical, honest account of driving myself across Namibia — Etosha's waterholes, Cape Cross's seals, sleeping on the roof of a 4x4, and everything I'd do again.</div>
            </a>
            <p className="wp-blurb" style={{ color: "var(--ink-soft)", fontSize: "0.88rem" }}>More articles are on their way — check back soon.</p>
          </div>
        )}

        {view === "products" && (
          <div>
            <h2 className="wp-section-title" style={{ marginBottom: "1.3rem" }}>{T.products}</h2>
            <div style={{ background: "#fff", border: "1px solid var(--hairline)", borderRadius: "10px", padding: "1.5rem 1.6rem", marginBottom: "1rem" }}>
              <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", fontSize: "0.85rem", color: "var(--gold)", fontWeight: 600, marginBottom: "0.6rem" }}><span style={{ width: 6, height: 6, borderRadius: "50%", background: "var(--gold)", display: "inline-block" }}></span>Free download</div>
              <div style={{ fontSize: "1.3rem", fontWeight: 600, marginBottom: "0.6rem" }}>Namibia Self-Drive Checklist &amp; Planner</div>
              <p style={{ fontSize: "0.95rem", color: "#4a4436", lineHeight: 1.6, marginBottom: "1.1rem" }}>The route at a glance, what to book months ahead, offline driving apps that actually work, and a gear checklist — everything from the Namibia trip report, organized into a printable planner.</p>
              <button
                onClick={() => goToStatic("newsletter")}
                style={{ display: "inline-block", background: "var(--navy)", color: "#fff", border: "none", cursor: "pointer", padding: "0.7rem 1.4rem", borderRadius: "11px", fontSize: "0.9rem", fontWeight: 600, fontFamily: "'Work Sans', sans-serif" }}
              >
                Get it free via the newsletter
              </button>
            </div>
            <p className="wp-blurb" style={{ color: "var(--ink-soft)", fontSize: "0.88rem" }}>More guides and planning tools are on their way — check back soon.</p>
          </div>
        )}

        {view === "about" && (
          <div className="wp-about">
            <h2 className="wp-section-title">{T.aboutMe}</h2>
            <div className="wp-about-top">
              <img src="foto-sobre-mim.png" alt="José Maria Garcia" className="wp-about-photo-img" />
              <div>
                {ABOUT_BIO[lang].map((para, i) => <p className="wp-about-bio" key={i}>{para}</p>)}
              </div>
            </div>
          </div>
        )}

        {view === "newsletter" && (
          <div className="wp-newsletter">
            <h2 className="wp-section-title">{T.newsletter}</h2>
            <p className="wp-blurb">{T.newsletterIntro}</p>
            <NewsletterSignupForm user={user} T={T} />
          </div>
        )}

        <footer className="wp-footer">
          <div className="wp-footer-top">
            <div className="wp-footer-brand">
              <div className="wp-brand-mark" style={{ width: 26, height: 26 }}><Compass size={14} style={{ color: "#F3EDE0" }} /></div>
              <div>
                <div className="wp-footer-brand-name">Waypoint</div>
                <div className="wp-footer-tagline">{T.footerTagline}</div>
              </div>
            </div>

            <div className="wp-footer-col">
              <div className="wp-footer-col-title">{T.footerExplore}</div>
              <button className="wp-footer-link" onClick={goToContinents}>{T.home}</button>
              <button className="wp-footer-link" onClick={() => goToStatic("articles")}>{T.articles}</button>
              <button className="wp-footer-link" onClick={() => goToStatic("products")}>{T.products}</button>
            </div>

            <div className="wp-footer-col">
              <div className="wp-footer-col-title">{T.footerConnect}</div>
              <button className="wp-footer-link" onClick={() => goToStatic("about")}>{T.aboutMe}</button>
              <button className="wp-footer-link" onClick={() => goToStatic("newsletter")}>{T.newsletter}</button>
              {/* Add real social links here once accounts exist, e.g.: <a className="wp-footer-link" href="https://instagram.com/...">Instagram</a> */}
            </div>
          </div>

          <div className="wp-footer-bottom">
            <span>© {new Date().getFullYear()} Waypoint</span>
            <span>{T.footerProjectBy} <a className="wp-footer-org-link" href="https://openforyou.org" target="_blank" rel="noopener noreferrer">OpenForYou.org</a></span>
            <a className="wp-footer-org-link" href="privacy-policy.html">Privacy Policy</a>
            <span>{T.footerBuiltFor}</span>
          </div>
        </footer>

        {showAuthModal && (
          <div className="wp-modal-overlay" onClick={closeAuthModal}>
            <div className="wp-auth-modal" onClick={(e) => e.stopPropagation()}>
              <button className="wp-modal-close" onClick={closeAuthModal} aria-label="Close"><X size={16} /></button>
              {showNewsletterNudge ? (
                <div>
                  <h2 className="wp-auth-title">{T.nudgeTitle}</h2>
                  <p className="wp-auth-subtitle">{T.nudgeSubtitle}</p>
                  <NewsletterSignupForm user={user} T={T} />
                  <button className="wp-auth-switch" onClick={closeAuthModal}>{T.nudgeSkip}</button>
                </div>
              ) : (
                <div>
                  <h2 className="wp-auth-title">{authMode === "signup" ? T.authModalTitleUp : T.authModalTitleIn}</h2>
                  <p className="wp-auth-subtitle">{T.authModalSubtitle}</p>

                  <button className="wp-google-btn" onClick={signInWithGoogle} disabled={authBusy}>
                    <GoogleG size={16} /> {T.continueWithGoogle}
                  </button>

                  <div className="wp-auth-divider"><span>{T.orDivider}</span></div>

                  <input
                    type="email"
                    className="wp-auth-input"
                    placeholder={T.emailLabel}
                    value={authEmail}
                    onChange={(e) => setAuthEmail(e.target.value)}
                  />
                  <input
                    type="password"
                    className="wp-auth-input"
                    placeholder={T.passwordLabel}
                    value={authPassword}
                    onChange={(e) => setAuthPassword(e.target.value)}
                    onKeyDown={(e) => { if (e.key === "Enter") submitAuthForm(); }}
                  />
                  {authError && <p className="wp-auth-error">{authError}</p>}

                  <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ width: "100%", justifyContent: "center", marginTop: "0.4rem" }} onClick={submitAuthForm} disabled={authBusy}>
                    {authMode === "signup" ? T.authSubmitSignUp : T.authSubmitSignIn}
                  </button>

                  <button className="wp-auth-switch" onClick={() => { setAuthMode(authMode === "signup" ? "signin" : "signup"); setAuthError(""); }}>
                    {authMode === "signup" ? T.authSwitchToSignIn : T.authSwitchToSignUp}
                  </button>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<Waypoint />);
"""
