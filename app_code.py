# -*- coding: utf-8 -*-
APP_CODE = r"""
const { useState, useEffect, useRef } = React;

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
    pctOfWorldVisited: "of the world visited",
    myTrips: "Trips", tripsSubtitle: "Plan your next trip, day by day.",
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
    pctOfWorldVisited: "do mundo visitado",
    myTrips: "Viagens", tripsSubtitle: "Planeia a tua próxima viagem, dia a dia.",
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
  if (!p) return c;
  return {
    ...c,
    name: p.name || c.name,
    capital: p.capital || c.capital,
    population: p.population || c.population,
    language: p.language || c.language,
    currency: p.currency || c.currency,
    bestTime: p.bestTime || c.bestTime,
    tagline: p.tagline || c.tagline,
    highlights: p.highlights || c.highlights,
    blurb: p.blurb || c.blurb,
    budget: p.budget || c.budget,
    visa: p.visa || c.visa,
    goodToKnow: p.goodToKnow || c.goodToKnow,
    food: p.food || c.food,
    attractions: c.attractions.map((a, i) => (p.attractions && p.attractions[i]) ? { ...a, name: p.attractions[i].name, desc: p.attractions[i].desc } : a),
    itinerary: c.itinerary.map((s, i) => (p.itinerary && p.itinerary[i]) ? {
      ...s,
      label: p.itinerary[i].label || s.label,
      title: p.itinerary[i].title || s.title,
      desc: p.itinerary[i].desc || s.desc,
      logistics: p.itinerary[i].logistics !== undefined ? p.itinerary[i].logistics : s.logistics,
    } : s),
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

    window.L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      attribution: '&copy; OpenStreetMap &copy; CARTO',
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
      window.L.marker([s.lat, s.lng], { icon }).addTo(map).bindTooltip(s.title || s.label, { direction: "top", offset: [0, -12] });
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

const WORLD_MAP_PATHS = {
  "botswana": "M1116.7,685l-1-0.5l-3.2,1.5h-1.6l-3.7,2.5l-2-2.6l-8.6,2.2l-4.1,0.2l-0.9,22.7l-5.4,0.2l-0.6,18.5l1.4,1l3,6.1 l-0.7,3.8l1.1,2.3l4-0.7l2.8-2.8l2.7-1.9l1.5-3.1l2.7-1.5l2.3,0.8l2.5,1.8l4.4,0.3l3.6-1.5l0.6-2l1.2-3l3-0.5l1.7-2.4l2-4.3l5.2-4.7 l8-4.7l-3.4-2.9l-4.2-0.9l-1.5-4.1l0.1-2.2l-2.3-0.7l-6-7l-1.6-3.7l-1.1-1.1L1116.7,685L1116.7,685z",
  "cabo-verde": "M841.4,477.6l0.1-0.4l-0.2-0.6l-0.3-0.1l-0.6,0.4l-0.1,0.3l0.1,0.3l0.3,0.3l0.3,0.1L841.4,477.6L841.4,477.6z M847.7,475.9l0.4-0.2V475l-0.1-0.3h-0.4l-0.2,0.4v0.1v0.4L847.7,475.9L847.7,475.9L847.7,475.9z M846.3,476.7l-0.5-0.9l-0.3-0.1 l-0.6-0.7v-0.3l-0.3-0.1v0.2v0.4l-0.2,0.5v0.5l0.4,0.8l0.4,0.2l0.7,0.1L846.3,476.7L846.3,476.7z M849.4,468.9v0.5l-0.3,0.7l0.5,0.3 l0.3,0.1l0.6-0.4l0.2-0.5l-0.1-0.3l-0.3-0.3l-0.3-0.1l-0.1,0.1L849.4,468.9L849.4,468.9z M843,466.4l-1-0.1l-0.6-0.2h-0.1v0.3 l0.4,0.8l0.2-0.5l0.2-0.1l0.8,0.2l0.4-0.1l-0.1-0.1L843,466.4L843,466.4z M849.7,466.2l-0.1-0.5V465h-0.2l-0.3,0.2l0.1,0.7l0.1,0.1 l0.2,0.5L849.7,466.2L849.7,466.2z M838.6,465.2V465l-0.3-0.5l-0.3,0.1l-0.4,0.2l-0.1,0.3l0.4,0.2h0.2L838.6,465.2L838.6,465.2z M837.1,464.3l0.8-0.6l0.2-0.3l-0.2-0.5l-0.5-0.1l-1.2,0.6l-0.1,0.2l0.1,0.3l0.1,0.5l0.2,0.1L837.1,464.3L837.1,464.3z",
  "egypt": "M1129.7,374.8l-5.5-1.9l-5.3-1.7l-7.1,0.2l-1.8,3l1.1,2.7l-1.2,3.9l2,5.1l1.3,22.7l1,23.4h22.1h21.4h21.8l-1-1.3 l-6.8-5.7l-0.4-4.2l1-1.1l-5.3-7l-2-3.6l-2.3-3.5l-4.8-9.9l-3.9-6.4l-2.8-6.7l0.5-0.6l4.6,9.1l2.7,2.9l2,2l1.2-1.1l1.2-3.3l0.7-4.8 l1.3-2.5l-0.7-1.7l-3.9-9.2l0,0l-2.5,1.6l-4.2-0.4l-4.4-1.5l-1.1,2.1l-1.7-3.2l-3.9-0.8l-4.7,0.6l-2.1,1.8l-3.9,2L1129.7,374.8 L1129.7,374.8z",
  "kenya": "M1211.7,547.2h-3.8l-2.3-2.1l-5.1,2.6l-1.6,2.7l-3.8-0.5l-1.2-0.7l-1.3,0.1h-1.8l-7.2-5.4h-3.9l-2-2.1v-3.6 l-2.9-1.1l-3.8,4.2l-3.4,3.8l2.7,4.4l0.7,3.2l2.6,7.3l-2.1,4.7l-2.7,4.2l-1.6,2.6v0.3l1.4,2.4l-0.4,4.7l20.2,13l0.4,3.7l8,6.3 l2.2-2.1l1.2-4.2l1.8-2.6l0.9-4.5l2.1-0.4l1.4-2.7l4-2.5l-3.3-5.3l-0.2-23.2L1211.7,547.2L1211.7,547.2z",
  "mauritius": "M1294.7,702.5l0.3-0.3l0.2-0.4l0.3-0.3l0.1-0.7l-0.2-0.8l-0.4-0.7l-0.5,0.1l-0.3,0.4l-0.2,0.5l-0.5,0.3l-0.1,0.3 l-0.2,0.7l-0.1,0.4l-0.2,0.1v0.2l0.3,0.3l0.8,0.1L1294.7,702.5L1294.7,702.5z",
  "morocco": "M965.2,348.4l-2.3-0.1l-5.5-1.4l-5,0.4l-3.1-2.7h-3.9l-1.8,3.9l-3.7,6.7l-4,2.6l-5.4,2.9L927,365l-0.9,3.4l-2.1,5.4 l1.1,7.9l-4.7,5.3l-2.7,1.7l-4.4,4.4l-5.1,0.7l-2.8,2.4l-0.1,0.1l-3.6,6.5l-3.7,2.3l-2.1,4l-0.2,3.3l-1.6,3.8l-1.9,1l-3.1,4l-2,4.5 l0.3,2.2l-1.9,3.3l-2.2,1.7l-0.3,3h0.1l12.4-0.5l0.7-2.3l2.3-2.9l2-8.8l7.8-6.8l2.8-8.1l1.7-0.4l1.9-5l4.6-0.7l1.9,0.9h2.5l1.8-1.5 l3.4-0.2l-0.1-3.4l0,0h0.8l0.1-7.5l8.9-4.7l5.4-1l4.4-1.7l2.1-3.2l6.3-2.5l0.3-4.7l3.1-0.5l2.5-2.4l7-1l1-2.5l-1.4-1.4l-1.8-6.7 l-0.3-3.9L965.2,348.4L965.2,348.4z",
  "namibia": "M1105.4,683.7l-10.3,2.5l-13.4-0.9l-3.7-3l-22.5,0.3l-0.9,0.4l-3.2-2.9l-3.6-0.1l-3.3,1l-2.7,1.2l0.2,4.9l4.4,6.2 l1.1,4l2.8,7.7l2.7,5.2l2.1,2.6l0.6,3.5v7.6l1.6,9.8l1.2,4.6l1,6.2l1.9,4.7l3.9,4.8l2.7-3.2l2.1,1.8l0.8,2.7l2.4,0.5l3.3,1.2 l2.9-0.5l5-3.2l1.1-23.6l0.6-18.5l5.4-0.2l0.9-22.7l4.1-0.2l8.6-2.2l2,2.6l3.7-2.5h1.6l3.2-1.5V684l-2.1-1.4l-3.6-0.4L1105.4,683.7 L1105.4,683.7z",
  "south-africa": "M1148.2,713.7l-2.9-0.6l-1.9,0.8l-2.6-1.1l-2.2-0.1l-8,4.7l-5.2,4.7l-2,4.3l-1.7,2.4l-3,0.5l-1.2,3l-0.6,2l-3.6,1.5 l-4.4-0.3l-2.5-1.8l-2.3-0.8l-2.7,1.5l-1.5,3.1l-2.7,1.9l-2.8,2.8l-4,0.7l-1.1-2.3l0.7-3.8l-3-6.1l-1.4-1l-1.1,23.6l-5,3.2l-2.9,0.5 l-3.3-1.2l-2.4-0.5l-0.8-2.7l-2.1-1.8l-2.7,3.2l3.5,8.2v0.1l2.5,5.3l3.2,6l-0.2,4.8l-1.7,1.2l1.4,4.2l-0.2,3.8l0.6,1.7l0.3-0.9 l2.1,2.9l1.8,0.1l2.1,2.3l2.4-0.2l3.5-2.4l4.6-1l5.6-2.5l2.2,0.3l3.3-0.8l5.7,1.2l2.7-1.2l3.2,1l0.8-1.8l2.7-0.3l5.8-2.5l4.3-2.9 l4.1-3.8l6.7-6.5l3.4-4.6l1.8-3.2l2.5-3.3l1.2-0.9l3.9-3.2l1.6-2.9l1.1-5.2l1.7-4.7h-4.1l-1.3,2.8l-3.3,0.7l-3-3.5l0.1-2.2l1.6-2.4 l0.7-1.8l1.6-0.5l2.7,1.2l-0.4-2.3l1.4-7.1l-1.1-4.5L1148.2,713.7L1148.2,713.7z M1128.1,766.5l-2,0.6l-3.7-4.9l3.2-4l3.1-2.5 l2.6-1.3l2.3,2l1.7,1.9l-1.9,3.1l-1.1,2.1l-3.1,1L1128.1,766.5L1128.1,766.5z",
  "tanzania": "M1149.6,578.6l-2,0.8l2.3,3.6l-0.4,3.7l-1.6,0.8l0,0l0.3,2.5l1.2,1.5v2l-1.4,1.4l-2.2,3.3l-2.1,2.3l-0.6,0.1 l-0.3,2.7l1.1,0.9l-0.2,2.7l1,2.6l-1.3,2.4l4.5,4.3l0.3,3.9l2.7,6.5l0,0l0.3,0.2l2.2,1.1l3.5,1.1l3.2,1.9l5.4,1.2l1.1,1.7l0,0 l0.4-1.2l2.8,3.4l0.3,6.7l1.8,2.4v0.1l2.1-0.3l6.7,1.8l1.4-0.8l3.9-0.1l2.1-1.9l3.3,0.1l6.2-2.5l4.6-3.7l0,0l-2-1.4l-2.2-6.3 l-1.8-3.9l0.4-3.1l-0.3-1.9l1.7-3.9l-0.2-1.6l-3.5-2.3l-0.3-3.6l2.8-7.9l-8-6.3l-0.4-3.7l-20.2-13l0,0l-2.8,2.8l-1.9,2.9l2.2,2.2 l-3.2,1.6l-0.7-0.8l-3.2,0.4l-2.5,1.4l-1.6-2.4l1.1-4.5l0.2-3.8l0,0l0,0L1149.6,578.6L1149.6,578.6z",
  "zambia": "M1128.6,626.8l-3-0.9l-4-3.4l-2.5,0.6l-1.9,2.5l-3-0.9l-3.9,2.4l-2.5-0.7l-1.5,1.6l-3.4-1.6l-3.2,2l-0.4,3.4l-3.3,1.7 l-1.8,4l-1.6,0.3l-1.8-1.9l-4.3,0.7l-2.4-1.3l-3,0.7l-3.5-2.6l0,0l-0.1,2.2l1.5,4.1l4.2,0.9l3.4,2.9l3.7,5.7l0,0l6.4-2l4.8,1.7 l3.5,4.1l1.5-1.1l3.4,0.3l0.9,2.4l3.6,0.3l1.4,3.1l-1.2,2.5l1.5,2.5l3.2,0.4l1.5,3.4l3.4-1.9l0.5-2.9l3.2-1.9l2.4-3.4l-0.1-2.5 l3.1-1.1l0.2-3.6l3.2-0.2l1.1-3l-1.5-3.6l1.3-2.3L1128.6,626.8L1128.6,626.8z",
  "zimbabwe": "M1128.6,668.7l-2.1-1l-1.9,1.4l-1.5,4l-3.8,0.5l-2.4,1.9l-4.1,0.4l-2.5-1.9l-4.4,1.6l-1.2-2.6l-4.9-1.8l-0.9-1.9 l-3-0.6l0,0l1.1,1.1l1.6,3.7l6,7l2.3,0.7l-0.1,2.2l1.5,4.1l4.2,0.9l3.4,2.9l1-0.5l3.4-1.9l1.6-3.2l4.5-2.6l0.4-4.9l1.6-2.2 L1128.6,668.7L1128.6,668.7z",
  "cambodia": "M1574.8,481.8l-5.2-2.3l-2,4.3l-4.9-2.4l-5.3-1l-7.1,1.3l-3,5.2l2.1,7.7l3.4,6.6l2.6,3.3l4.7,0.9l4.7-2.5l5.8-0.5 l-2.8-3.8l8.9-4.9l-0.1-7.7L1574.8,481.8L1574.8,481.8z",
  "china": "M1587.2,453.3l0.6-3.6l2-2.8l-1.6-2.5l-3.2-0.1l-5.8,1.8l-2.2,2.8l1,5.5l4.9,2L1587.2,453.3L1587.2,453.3z M1600.4,256.8l-6.1-6.1l-4.4-3.7l-3.8-2.7l-7.7-6.1l-5.9-2.3l-8.5-1.8l-6.2,0.2l-5.1,1.1l-1.7,3l3.7,1.5l2.5,3.3l-1.2,2l0.1,6.5 l1.9,2.7l-4.4,3.9l-7.3-2.3l0.6,4.6l0.3,6.2l2.7,2.6l2.4-0.8l5.4,1l2.5-2.3l5.1,2l7.2,4.3l0.7,2.2l-4.3-0.7l-6.8,0.8l-2.4,1.8 l-1.4,4.1l-6.3,2.4l-3.1,3.3l-5.9-1.3l-3.2-0.5l-0.4,4l2.9,2.3l1.9,2.1l-2.5,2l-1.9,3.3l-4.9,2.2l-7.5,0.2l-7.2,2.2l-4.4,3.3l-3.2-2 l-6.2,0.1l-9.3-3.8l-5.5-0.9l-6.4,0.8l-11.2-1.3l-5.5,0.1l-4.7-3.6l-4.9-5.7l-3.4-0.7l-7.9-3.8l-7.2-0.9l-6.4-1l-3-2.7l-1.3-7.3 l-5.8-5l-8.1-2.3l-5.7-3.3l-3.3-4.4l-1.7,0.5l-1.8,4.2l-3.8,0.6l2.5,6.2l-1.6,2.8l-10.7-2l1,11.1l-2,1.4l-9,2.4l8.7,10.7l-2.9,1.6 l1.7,3.5l-0.2,1.4l-6.8,3.4l-1,2.4l-6.4,0.8l-0.6,4l-5.7-0.9l-3.2,1.2l-4,3l1.1,1.5l-1,1.5l3,5.9l1.6-0.6l3.5,1.4l0.6,2.5l1.8,3.7 l1.4,1.9l4.7,3l2.9,5l9.4,2.6l7.6,7.5l0.8,5.2l3,3.3l0.6,3.3l-4.1-0.9l3.2,7l6.2,4l8.5,4.4l1.9-1.5l4.7,2l6.4,4.1l3.2,0.9l2.5,3.1 l4.5,1.2l5,2.8l6.4,1.5l6.5,0.6l3-1.4l1.5,5.1l2.6-4.8l2.6-1.6l4.2,1.5l2.9,0.1l2.7,1.8l4.2-0.8l3.9-4.8l5.3-4l4.9,1.5l3.2-2.6 l3.5,3.9l-1.2,2.7l6.1,0.9l3-0.4l2.7,3.7l2.7,1.5l1.3,4.9l0.8,5.3l-4.1,5.3l0.7,7.5l5.6-1l2.3,5.8l3.7,1.3l-0.8,5.2l4.5,2.4l2.5,1.2 l3.8-1.8l0.6,2.6l0.7,1.5l2.9,0.1l-1.9-7.2l2.7-1l2.7-1.5h4.3l5.3-0.7l4.1-3.4l3,2.4l5.2,1.1l-0.2,3.7l3,2.6l5.9,1.6l2.4-1l7.7,2 l-0.9,2.5l2.2,4.6l3-0.4l0.8-6.7l5.6-0.9l7.2-3.2l2.5-3.2l2.3,2.1l2.8-2.9l6.1-0.7l6.6-5.3l6.3-5.9l3.3-7.6l2.3-8.4l2.1-6.9l2.8-0.5 l-0.1-5.1l-0.8-5.1l-3.8-2l-2.5-3.4l2.8-1.7l-1.6-4.7l-5.4-4.9l-5.4-5.8l-4.6-6.3l-7.1-3.5l0.9-4.6l3.8-3.2l1-3.5l6.7-1.8l-2.4-3.4 l-3.4-0.2l-5.8-2.5l-3.9,4.6l-4.9-1.9l-1.5-2.9l-4.7-1l-4.7-4.4l1.2-3l5-0.3l1.2-4.1l3.6-4.4l3.4-2.2l4.4,3.3l-1.9,4.2l2.3,2.5 l-1.4,3l4.8-1.8l2.4-2.9l6.3-1.9l2.1-4l3.8-3.4l1-4.4l3.6,2l4.6,0.2l-2.7-3.3l6.3-2.6l-0.1-3.5l5.5,3.6l0,0l-1.9-3.1l2.5-0.1 l-3.8-7.3l-4.7-5.3l2.9-2.2l6.8,1.1l-0.6-6l-2.8-6.8l0.4-2.3l-1.3-5.6l-6.9,1.8l-2.6,2.5h-7.5l-6-5.8l-8.9-4.5L1600.4,256.8 L1600.4,256.8z",
  "india": "M1414.1,380.1l-8.5-4.4l-6.2-4l-3.2-7l4.1,0.9l-0.6-3.3l-3-3.3l-0.8-5.2l-7.6-7.5l-3.7,5.4l-5.7,1l-8.5-1.6 l-1.9,2.8l3.2,5.6l2.9,4.3l5,3.1l-3.7,3.7l1,4.5l-3.9,6.3l-2.1,6.5l-4.5,6.7l-6.4-0.5l-4.9,6.6l4,2.9l1.3,4.9l3.5,3.2l1.8,5.5h-12 l-3.2,4.2l7.1,5.4l1.9,2.5l-2.4,2.3l8,7.7l4,0.8l7.6-3.8l1.7,5.9l0.8,7.8l2.5,8.1l3.6,12.3l5.8,8.8l1.3,3.9l2,8l3.4,6.1l2.2,3 l2.5,6.4l3.1,8.9l5.5,6l2.2-1.8l1.7-4.4l5-1.8l-1.8-2.1l2.2-4.8l2.9-0.3l-0.7-10.8l1.9-6.1l-0.7-5.3l-1.9-8.2l1.2-4.9l2.5-0.3 l4.8-2.3l2.6-1.6l-0.3-2.9l5-4.2l3.7-4l5.3-7.5l7.4-4.2l2.4-3.8l-0.9-4.8l6.6-1.3l3.7,0.1l0.5-2.4l-1.6-5.2l-2.6-4.8l0.4-3.8 l-3.7-1.7l0.8-2.3l3.1-2.4l-4.6-3.4l1.2-4.3l4.8,2.7l2.7,0.4l1.2,4.4l5.4,0.9l5-0.1l3.4,1.1l-1.6,5.3l-2.4,0.4l-1.1,3.6l3.5,3.3 l0.2-4l1.5-0.1l4.5,10.1l2.4-1.5l-0.9-2.7l0.9-2.1l-0.9-6.6l4.6,1.4l1.5-5.2l-0.3-3.1l2.1-5.4l-0.9-3.6l6.1-4.4l4.1,1.1l-1.3-3.9 l1.6-1.2l-0.9-2.4l-6.1-0.9l1.2-2.7l-3.5-3.9l-3.2,2.6l-4.9-1.5l-5.3,4l-3.9,4.8l-4.2,0.8l2.7,2l0.4,3.9l-4.4,0.2l-4.7-0.4l-3.2,1 l-5.5-2.5l-0.3-1.2l-1.5-5.1l-3,1.4l0.1,2.7l1.5,4.1l-0.1,2.5l-4.6,0.1l-6.8-1.5l-4.3-0.6l-3.8-3.2l-7.6-0.9l-7.7-3.5l-5.8-3.1 l-5.7-2.5l0.9-5.9L1414.1,380.1L1414.1,380.1z",
  "indonesia": "M1651.9,637.3l0.5-1.7l-1.8-1.9l-2.8-2l-5.3,1.3l7,4.4L1651.9,637.3L1651.9,637.3z M1672.8,636.7l4-4.8l0.1-1.9 l-0.5-1.3l-5.7,2.6l-2.8,3.9l-0.7,2.1l0.6,0.8L1672.8,636.7L1672.8,636.7z M1637.2,623.7l-1.6,2.2l-3.1,0.1l-2.2,3.6l3,0.1l3.9-0.9 l6.6-1.2l-1.2-2.8l-3.5,0.6L1637.2,623.7L1637.2,623.7z M1665.3,623.7l-5.2,2.3l-3.8,0.5l-3.4-1.9l-4.5,1.3l-0.2,2.3l7.4,0.8 l8.6-1.8L1665.3,623.7L1665.3,623.7z M1585.8,615.3l-0.7-2.3l-2.3-0.5l-4.4-2.4l-6.8-0.4l-4.1,6.1l5.1,0.4l0.8,2.8l10,2.6l2.4-0.8 l4.1,0.6l6.3,2.4l5.2,1.2l5.8,0.5l5.1-0.2l5.9,2.5l6.6-2.4l-6.6-3.8l-8.3-1.1l-1.8-4.1l-10.3-3.1l-1.3,2.6L1585.8,615.3 L1585.8,615.3z M1732.4,611.7l0.2-3l-1.2-1.9l-1.3,2.2l-1.2,2.2l0.3,4.8L1732.4,611.7z M1691.4,594.2l-1.4-2.1l-5.7,0.3l1,2.7 l3.9,1.2L1691.4,594.2L1691.4,594.2z M1709.5,591.8l-6.1-1.8l-6.9,0.3l-1.5,3.5l3.9,0.2l3.2-0.4l4.6,0.5l4.7,2.6L1709.5,591.8 L1709.5,591.8z M1730.5,579.5l-0.8-2.4l-9-2.6l-2.9,2.1l-7.6,1.5l2.3,3.2l5,1.2l2.1,3.7l8.3,0.1l0.4,1.6l-4-0.1l-6.2,2.3l4.2,3.1 l-0.1,2.8l1.2,2.3l2.1-0.5l1.8-3.1l8.2,5.9l4.6,0.5l10.6,5.4l2.3,5.3l1,6.9l-3.7,1.8l-2.8,5.2l7.1-0.2l1.6-1.8l5.5,1.3l4.6,5.2 l1.5-20.8l1-20.7l-6-1.2l-4.1-2.3l-4.7-2.2h-5l-6.6,3.8l-4.9,6.8l-5.7-3.8L1730.5,579.5z M1680.5,563.1l-1-1.4l-5.5,4.6l-6.5,0.3 l-7.1-0.9l-4.4-1.9l-4.7,4.8l-1.2,2.6l-2.9,9.6l-0.9,5l-2.4,4.2l1.6,4.3l2.3,0.1l0.6,6.1l-1.9,5.9l2.3,1.9l3.6-1l0.3-9.1l-0.2-7.4 l3.8-1.9l-0.7,6.2l3.9,3.7l-0.8,2.5l1.3,1.7l5.6-2.4l-3,5.2l2.1,2.2l3.1-1.9l0.3-4.1l-4.7-7.4l1.1-2.2l-5.1-8.1l5-2.5l2.6-3.7 l2.4,0.9l0.5-2.9l-10.5,2.1l-3.1,2.9l-5-5.6l0.9-4.8l4.9-1l9.3-0.3l5.4,1.3l4.3-1.3L1680.5,563.1L1680.5,563.1z M1699.9,565 l-0.6-2.6l-3.3-0.6l-0.5-3.5l-1.8,2.3l-1,5.1l1.7,8.2l2.2,4l1.6-0.8l-2.3-3.3l0.9-3.9l2.9,0.6L1699.9,565L1699.9,565z M1639,560.5 l0.9-2.9l-4.3-6l3-5.8l-5-1h-6.4l-1.7,7.2l-2,2.2l-2.7,8.9l-4.5,1.3l-5.4-1.8l-2.7,0.6l-3.2,3.2l-3.6-0.4l-3.6,1.2l-3.9-3.5l-1-4.3 l-3.3,4.2l-0.6,5.9l0.8,5.6l2.6,5.4l2.8,1.8l0.7,8.5l4.6,0.8l3.6-0.4l2,3.1l6.7-2.3l2.8,2l4,0.4l2,3.9l6.5-2.9l0.8,2.3l2.5-9.7 l0.3-6.4l5.5-4.3l-0.2-5.8l1.8-4.3l6.7-0.8L1639,560.5L1639,560.5z M1570.3,609.4l0.7-9.8l1.7-8l-2.6-4l-4.1-0.5l-1.9-3.6l-0.9-4.4 l-2-0.2l-3.2-2.2l2.3-5.2l-4.3-2.9l-3.3-5.3l-4.8-4.4l-5.7-0.1l-5.5-6.8l-3.2-2.7l-4.5-4.3l-5.2-6.2l-8.8-1.2l-3.6-0.3l0.6,3.2 l6.1,7l4.4,3.6l3.1,5.5l5.1,4l2.2,4.9l1.7,5.5l4.9,5.3l4.1,8.9l2.7,4.8l4.1,5.2l2.2,3.8l7,5.2l4.5,5.3L1570.3,609.4L1570.3,609.4z",
  "japan": "M1692.5,354.9l-4.5-1.3l-1.1,2.7l-3.3-0.8l-1.3,3.8l1.2,3l4.2,1.8l-0.1-3.7l2.1-1.5l3.1,2.1l1.3-3.9L1692.5,354.9 L1692.5,354.9z M1716.9,335.6l-3.6-6.7l1.3-6.4l-2.8-5.2l-8.1-8.7l-4.8,1.2l0.2,3.9l5.1,7.1l1,7.9l-1.7,2.5l-4.5,6.5l-5-3.1v11.5 l-6.3-1.3l-9.6,1.9l-1.9,4.4l-3.9,3.3l-1.1,4l-4.3,2l4,4.3l4.1,1.9l0.9,5.7l3.5,2.5l2.5-2.7l-0.8-10.8l-7.3-4.7l6.1-0.1l5-3l8.6-1.4 l2.4,4.8l4.6,2.4l4.4-7.3l9.1-0.4l5.4-3l0.6-4.6l-2.5-3.2L1716.9,335.6L1716.9,335.6z M1705.1,291.4l-5.3-2.1l-10.4-6.4l1.9,4.8 l4.3,8.5l-5.2,0.4l0.6,4.7l4.6,6.1h5.7l-1.6-6.8l10.8,4.2l0.4-6.1l6.4-1.7l-6-6.9l-1.7,2.6L1705.1,291.4L1705.1,291.4z",
  "kuwait": "M1235.6,381.4l-3.7-0.5l-3.2,6.1l4.9,0.6l1.7,3.1l3.8-0.2l-2.4-4.8l0.3-1.5L1235.6,381.4L1235.6,381.4z",
  "laos": "M1574.8,481.8l0.2-6.4l-2-4.5l-4.8-4.4l-4.3-5.6l-5.7-7.5l-7.3-3.8l1.3-2.3l3.3-1.7l-3-5.5l-6.8-0.1l-3.4-5.7 l-4-5.1l-2.7,1l1.9,7.2l-2.9-0.1l-0.7-1.5l-4.1,4.1l-0.8,2.4l2.6,1.9l0.9,3.8l3.8,0.3l-0.4,6.7l1,5.7l5.3-3.8l1.8,1.2l3.2-0.2 l0.8-2.2l4.3,0.4l4.9,5.2l1.3,6.3l5.2,5.5l0.5,5.4l-1.5,2.9l4.9,2.4l2-4.3L1574.8,481.8L1574.8,481.8z",
  "malaysia": "M1558.1,554.4l-0.5-3.8l-0.6-2.1l0.5-2.9l-0.5-4.3l-2.6-4.3l-3.5-3.8l-1.3-0.6l-1.7,2.6l-3.7,0.8l-0.6-3.3l-4.7-2.8 l-0.9,1.1l1.4,2.7l-0.4,4.7l2.1,3.4l1,5.3l3.4,4.3l0.8,3.2l6.7,5l5.4,4.8l4-0.5l0.1-2.1l-2.3-5.6L1558.1,554.4z M1560.9,563.3 l0.2,0.2l-0.1,0.2l-0.9,0.4l-0.9-0.4l0.3-0.6l0.6-0.1l0.5,0.2L1560.9,563.3z M1645.2,540.2l-3.8,0.4l1.2,3.1l-4,2.1l-5-1h-6.4 l-1.7,7.2l-2,2.2l-2.7,8.9l-4.5,1.3l-5.4-1.8l-2.7,0.6l-3.2,3.2l-3.6-0.4l-3.6,1.2l-3.9-3.5l-1-4.3l4.1,2.2l4.4-1.2l0.9-5.4l2.4-1.2 l6.7-1.4l3.8-5l2.6-4l2.7,3.3l1.1-2.2l2.7,0.2l0.1-4.1l0.1-3.1l4.1-4.4l2.5-5h2.3l3.1,3.2l0.4,2.8l3.8,1.7l4.8,2L1645.2,540.2z",
  "oman": "M1301,437.8l2.1-2l0.8-1.8l1.6-3.8l-0.1-1.4l-2.1-0.8l-1.6-2.1l-2.9-3.7l-3.3-1.1l-4.1-0.9l-3.3-2.3l-2.9-4.3h-2.8 l-0.1,4.2l1.1,0.8l-2.4,1.3l0.3,2.6l-1.4,2.6l0.1,2.6l2.9,4.5l-2.6,12.7l-16.1,6.4l5.2,10.5l2.1,4.4l2.5-0.3l3.6-2.2l3.1,0.6 l2.5-1.8l-0.2-2.5l2.1-1.6h3.4l1.2-1.3l0.2-3.1l3.3-2.4h2.6l0.4-0.8l-1-4.2l0.6-3.2l1-1.5l2.5,0.3L1301,437.8L1301,437.8z M1284.4,407.4l0.2-2.6l-0.7-0.6l-1.3,2.2l1.3,2.2L1284.4,407.4z",
  "qatar": "M1258,415.5l0.8-3.8l-0.5-3.7l-1.9-2l-1.4,0.7l-1.1,3.3l0.8,4.7l1.8,1.2L1258,415.5L1258,415.5z",
  "singapore": "M1561,563.7l0.1-0.2l-0.2-0.2l-0.3-0.1l-0.5-0.2l-0.6,0.1l-0.3,0.6l0.9,0.4L1561,563.7L1561,563.7z",
  "thailand": "M1562.7,481.4l1.5-2.9l-0.5-5.4l-5.2-5.5l-1.3-6.3l-4.9-5.2l-4.3-0.4l-0.8,2.2l-3.2,0.2l-1.8-1.2l-5.3,3.8l-1-5.7 l0.4-6.7l-3.8-0.3l-0.9-3.8l-2.6-1.9l-3,1.4l-2.8,2.8l-3.9,0.3l-1.5,6.9l-2.2,1.1l3.5,5.6l4.1,4.6l2.9,4.2l-1.4,5.6l-1.7,1.1 l1.7,3.2l4.2,5.1l1,3.5l0.2,3l2.8,5.8l-2.6,5.9l-2.2,6.6l-1.3,6.1l-0.3,3.9l1.2,3.6l0.7-3.8l2.9,3.1l3.2,3.5l1.1,3.2l2.4,2.4 l0.9-1.1l4.7,2.8l0.6,3.3l3.7-0.8l1.7-2.6l-3.1-3.3l-3.4-0.8l-3.3-3.6l-1.4-5.5l-2.6-5.8l-3.7-0.2l-0.7-4.6l1.4-5.6l2.2-9.3l-0.2-7 l4.9-0.1l-0.3,5l4.7-0.1l5.3,2.9l-2.1-7.7l3-5.2l7.1-1.3L1562.7,481.4L1562.7,481.4z",
  "uae": "M1283.9,408.6l-1.3-2.2l-3,3.9l-3.7,4.1l-3.3,4.3l-3.3-0.2l-4.6-0.2l-4.2,1l-0.3-1.7l-1,0.3l0.4,1.5l2.6,6.4 l16.8,3.2l1-1.3l-0.1-2.6l1.4-2.6l-0.3-2.6l2.4-1.3l-1.1-0.8l0.1-4.2h2.8L1283.9,408.6L1283.9,408.6z",
  "vietnam": "M1567.7,463.6l-3.4-6.9l0.2-3l-2.2-1.8l-2.3,0.8l-2.5,3.2l-3-0.1l0.3,3.2l3.1,4.4l1.6,1l0.7,3.8l3.2,4.2l0.8,3.4 l-2.1,3.9l1.5,4.6l1.9,2.2l2.6,7.5l-0.8,3.9l2.9,7.3l3.2,3.5l1.1,3.7l3.1,1.4l-0.8-5l-2.9-6.6l0.2-2.9l-2.4-4.5l0.2-2.6l-1.9-3 l-1.8-4.4l0.4-4.4l-2.1-4.2l0.2-3.4l-1.6-2.8L1567.7,463.6L1567.7,463.6z",
  "austria": "M1060.2,264l-2.3-1.2l-2.3,0.3l-4-1.9l-1.7,0.5l-2.6,2.5l-3.8-2l-1.5,2.9l-1.7,0.8l1,4l-0.4,1.1l-1.7-1.3l-2.4-0.2 l-3.4,1.2l-4.4-0.3l-0.6,1.6l-2.6-1.7l-1.5,0.3l0.2,1.1l-0.7,1.6l2.3,1.1l2.6,0.2l3.1,0.9l0.5-1.2l4.8-1.1l1.3,2.2l7.2,1.6l4.2,0.4 l2.4-1.4l4.3-0.1l0.9-1.1l1.3-4l-1.1-1.3h2.8l0.2-2.6l-0.7-2.1L1060.2,264L1060.2,264z",
  "belgium": "M1000.7,246.2l-4.4,1.3l-3.6-0.5l0,0l-3.8,1.2l0.7,2.2l2.2,0.1l2.4,2.4l3.4,2.9l2.5-0.4l4.4,2.8l0.4-3.5l1.3-0.2 l0.4-4.2l-2.8-1.4L1000.7,246.2L1000.7,246.2z",
  "bosnia": "M1062.2,284.9l-2.3,0.1l-1,1.3l-1.9-1.4l-0.9,2.5l2.7,2.9l1.3,1.9l2.5,2.3l2,1.4l2.2,2.5l4.7,2.4l0.4-3.4l1.5-1.4 l0.9-0.6l1.2-0.3l0.5-2.9l-2.7-2.3l1-2.7h-1.8l0,0l-2.4-1.4l-3.5,0.1L1062.2,284.9L1062.2,284.9z",
  "croatia": "M1065,280.4l-4-2.6l-1.6-0.8l-3.9,1.7l-0.3,2.5l-1.7,0.6l0.2,1.7l-2-0.1l-1.8-1l-0.8,1l-3.5-0.2l-0.2,0.1v2.2l1.7,2 l1.3-2.6l3.3,1l0.3,2l2.5,2.6l-1,0.5l4.6,4.5l4.8,1.8l3.1,2.2l5,2.3l0,0l0.5-1l-4.7-2.4l-2.2-2.5l-2-1.4l-2.5-2.3l-1.3-1.9l-2.7-2.9 l0.9-2.5l1.9,1.4l1-1.3l2.3-0.1l4.4,1l3.5-0.1l2.4,1.4l0,0l1.7-2.3l-1.7-1.8l-1.5-2.4l0,0l-1.8,0.9L1065,280.4L1065,280.4z",
  "czech-republic": "M1049.4,248.5l-2.1,0.6l-1.4-0.7l-1.1,1.2l-3.4,1.2l-1.7,1.5l-3.4,1.3l1,1.9l0.7,2.6l2.6,1.5l2.9,2.6l3.8,2l2.6-2.5 l1.7-0.5l4,1.9l2.3-0.3l2.3,1.2l0.6-1.4l2.2,0.1l1.6-0.6l0.1-0.6l0.9-0.3l0.2-1.4l1.1-0.3l0.6-1.1h1.5l-2.6-3.1l-3.6-0.3l-0.7-2 l-3.4-0.6l-0.6,1.5l-2.7-1.2l0.1-1.7l-3.7-0.6L1049.4,248.5L1049.4,248.5z",
  "denmark": "M1035.9,221.2l-1.7-3l-6.7,2l0.9,2.5l5.1,3.4L1035.9,221.2L1035.9,221.2z M1027.3,216.1l-2.6-0.9l-0.7-1.6l1.3-2 l-0.1-3l-3.6,1.6l-1.5,1.7l-4,0.4l-1.2,1.7l-0.7,1.6l0.4,6.1l2.1,3.4l3.6,0.8l3-0.9l-1.5-3l3.1-4.3l1.4,0.7L1027.3,216.1 L1027.3,216.1z",
  "france": "M1012.2,290.9l2.7,0.8l-0.5,2.7l-0.1,0.1l-0.3-0.2l-0.5,0.6l0,0.3l-3.6,2.6l-10-1.6l-7.4,2l-0.5,3.7l-6,0.8 l-1.3-0.7l0.7-0.3l0.2-0.4l-0.2-0.2l-0.7-0.2l-0.3-0.1l-0.4,0.3l-0.1,0.3l0.1,0.1v0.2l-3.7-1.8l-1.9,1.3l-9.4-2.8l-2-2.4l2.7-3.7 l1-12.3l-5.1-6.5l-3.6-3.1l-7.5-2.4l-0.4-4.6l6.4-1.3l8.2,1.6l-1.4-7l4.6,2.6l11.3-4.8l1.4-5.1l4.3-1.2l0.7,2.2l2.2,0.1l2.4,2.4 l3.4,2.9l2.5-0.4l4.4,2.8l0,0l1.1,0.5l1.4-0.1l2.4,1.6l7.1,1.2l-2.3,4.2l-0.5,4.5l-1.3,1l-2.3-0.6l0.2,1.6l-3.5,3.5v2.8l2.4-0.9 l1.8,2.7l0,0l-0.2,1.7l1.6,2.4l-1.7,1.8L1012.2,290.9z M1025.6,304.3l-1-6l-0.6,1.6l-2.7,1.1l-0.7,4.3l3,3.7L1025.6,304.3z",
  "georgia": "M1200,300.2l-7.5-2.9l-7.7-1l-4.5-1.1l-0.5,0.7l2.2,1.9l3,0.7l3.4,2.3l2.1,4.2l-0.3,2.7l5.4-0.3l5.6,3l6.9-1l1.1-1 l4.2,1.8l2.8,0.4l0.6-0.7l-3.2-3.4l1.1-0.9l-3.5-1.4l-2.1-2.5l-5.1-1.3l-2.9,1L1200,300.2L1200,300.2z",
  "germany": "M1043.6,232.3l-2.4-1.9l-5.5-2.4l-2.5,1.7l-4.7,1.1l-0.1-2.1l-4.9-1.4l-0.2-2.3l-3,0.9l-3.6-0.8l0.4,3.4l1.2,2.2 l-3,3l-1-1.3l-3.9,0.3l-0.9,1.3l1,2l-1,5.6l-1.1,2.3h-2.9l1.1,6.4l-0.4,4.2l1,1.4l-0.2,2.7l2.4,1.6l7.1,1.2l-2.3,4.2l-0.5,4.5h4.2 l1-1.4l5.4,1.9l1.5-0.3l2.6,1.7l0.6-1.6l4.4,0.3l3.4-1.2l2.4,0.2l1.7,1.3l0.4-1.1l-1-4l1.7-0.8l1.5-2.9l-2.9-2.6l-2.6-1.5l-0.7-2.6 l-1-1.9l3.4-1.3l1.7-1.5l3.4-1.2l1.1-1.2l1.4,0.7l2.1-0.6l-2.3-3.9l0.1-2.1l-1.4-3.3l-2-2.2l1.2-1.6L1043.6,232.3L1043.6,232.3z",
  "greece": "M1101.9,344.9l-0.8,2.8l6.6,1.2v1.1l7.6-0.6l0.5-1.9l-2.8,0.8v-1.1l-3.9-0.5l-4.1,0.4L1101.9,344.9L1101.9,344.9z M1113.4,307.5l-2.7-1.6l0.3,3l-4.6,0.6l-3.9-2.1l-3.9,1.7l-3.8-0.2l-1,0.2l-0.7,1.1l-2.8-0.1l-1.9,1.3l-3.3,0.6v1.6l-1.6,0.9 l-0.1,2.1l-2.1,3l0.5,1.9l2.9,3.6l2.3,3l1.3,4.3l2.3,5.1l4.6,2.9l3.4-0.1l-2.4-5.7l3.3-0.7l-1.9-3.3l5,1.7l-0.4-3.7l-2.7-1.8l-3.2-3 l1.8-1.4l-2.8-3l-1.6-3.8l0.9-1.3l3,3.2h2.9l2.5-1l-3.9-3.6l6.1-1.6l2.7,0.6l3.2,0.2l1.1-0.7L1113.4,307.5L1113.4,307.5z",
  "iceland": "M915.7,158.6l-6.9-0.4l-7.3,2.9l-5.1-1.5l-6.9,3l-5.9-3.8l-6.5,0.8l-3.6,3.7l8.7,1.3l-0.1,1.6l-7.8,1.1l8.8,2.7 l-4.6,2.5l11.7,1.8l5.6,0.8l3.9-1l12.9-3.9l6.1-4.2l-4.4-3.8L915.7,158.6L915.7,158.6z",
  "ireland": "M947.3,231.7l-3.5-1.3l-2.9,0.1l1.1-3.2l-0.8-3.2l-3.7,2.8l-6.7,4.7l2.1,6.1l-4.2,6.4l6.7,0.9l8.7-3.6l3.9-5.4 L947.3,231.7L947.3,231.7z",
  "italy": "M1057.8,328.6l-1.6,5.1l0.9,2l-0.9,3.3l-4.2-2.4l-2.7-0.7l-7.5-3.3l0.6-3.4l6.2,0.6l5.2-0.7L1057.8,328.6z M1072.3,316.2l-0.8,2.3l-3.1-3l-4.5-1l-1.9,4.1l3.9,2.3l-0.4,3.3l-2.1,0.4l-2.5,5.6l-2.1,0.5l-0.1-2l0.8-3.5l1.1-1.3l-2.3-3.7 l-1.8-3.2l-2.2-0.8l-1.7-2.7l-3.4-1.2l-2.3-2.5l-3.9-0.4l-4.2-2.8l-4.9-4l-3.6-3.6l-1.9-6l-2.6-0.7l-4.2-2.1l-2.3,0.9l-2.8,2.8 l-2.1,0.5l0.5-2.7l-2.7-0.8l-1.5-4.8l1.7-1.8l-1.6-2.4l0.2-1.7l2.2,1.3l2.4-0.3l2.7-2.1l0.9,1l2.4-0.2l0.9-2.5l3.8,0.8l2.1-1.1 l0.3-2.5l3.1,0.9l0.5-1.2l4.8-1.1l1.3,2.2l7.2,1.6l-0.3,3l1.4,2.7l-4.1-0.9l-3.9,2.2l0.4,3l-0.5,1.8l1.9,3.1l4.9,3.1l2.9,5.1l6,5 l4-0.1l1.4,1.4l-1.4,1.2l4.8,2.3l3.9,1.9l4.7,3.2L1072.3,316.2z M1040.2,305.3l-0.1-0.6l-0.6,0.1l-0.2,0.5H1040.2z M1040.3,292.4 l-0.9,0.3l0.2,0.9l0.7-0.1L1040.3,292.4z M1021.6,311.6l-2.8-0.3l1.3,3.6l0.4,7.6l2.1,1.7l2-2.1l2.4,0.4l0.4-8.4l-3.3-4.4 L1021.6,311.6z",
  "liechtenstein": "M1024.4,273.6v-0.2l0.1-0.2l-0.1-0.1l-0.1-0.2l-0.1-0.1v-0.2l-0.1-0.1v-0.2l-0.1-0.1l-0.2,0.6v0.5l0.1,0.2h0.1 L1024.4,273.6L1024.4,273.6z",
  "luxembourg": "M1007,258.6l0.2-2.7l-1-1.4l-1.3,0.2l-0.4,3.5l1.1,0.5L1007,258.6z",
  "monaco": "M1013.5,295.2l0-0.3l0.5-0.6l0.3,0.2L1013.5,295.2z",
  "netherlands": "M1005.5,243.9h2.9l1.1-2.3l1-5.6l-1-2l-3.9-0.2l-6.5,2.6l-3.9,8.9l-2.5,1.7l0,0l3.6,0.5l4.4-1.3l3.1,2.7l2.8,1.4 L1005.5,243.9L1005.5,243.9z",
  "north-macedonia": "M1094,304.8l-2.8-2l-2.4,0.1l-1.7,0.4l-1.1,0.2l-2.9,1l-0.1,1.2h-0.7l0,0l-0.4,2.1l0.9,2.6l2.3,1.6l3.3-0.6l1.9-1.3 l2.8,0.1l0.7-1.1l1-0.2L1094,304.8L1094,304.8z",
  "norway": "M1088.8,133.1l-6.9,1.1l-7.3-0.3l-5.1,4.4l-6.7-0.3l-8.5,2.3l-10.1,6.8l-6.4,4l-8.8,10.7l-7.1,7.8l-8.1,5.8 l-11.2,4.8l-3.9,3.6l1.9,13.4l1.9,6.3l6.4,3l6-1.4l8.5-6.8l3.3,3.6l1.7-3.3l3.4-4l0.9-6.9l-3.1-2.9l-1-7.6l2.3-5.3l4.3,0.1l1.3-2.2 l-1.8-1.9l5.7-7.9l3.4-6.1l2.2-3.9l4,0.1l0.6-3.1l7.9,0.9v-3.5l2.5-0.3l2.1-1.4l5.1,2.9l5.3-0.3l4.7,1.3l3.4-2.4l1.1-3.9l5.8-1.8 l5.7,2.1l-0.8,3.8l3.2-0.5l6.4-2.2l0,0l-5.4-3.3l4.8-1.4L1088.8,133.1L1088.8,133.1z M1066.2,99.8l-5.6-1l-1.9-1.7l-7.2,0.9l2.6,1.5 l-2.2,1.2l6.7,1.1L1066.2,99.8z M1040.8,91.5l-4.8-1.6l-5.1,0.2l-1,1.5h-5l-2.2-1.5l-9.3,1.6l3.2,3.5l7.6,3.8l5.7,1.4l-3,1.7 l8.4,2.9l4.4-0.2l0.9-3.9l3-0.9l1.2-3.4l8.5-1.8C1053.3,94.8,1040.8,91.5,1040.8,91.5z M1065,88.4l-9.1-1l-3.2,1.2l-5.3-1l-10.4,1.2 l4.3,2h5.1l0.9,1.3l10.6,0.7l10.1-0.5l4.3-2.4C1072.3,89.9,1065,88.4,1065,88.4z",
  "poland": "M1069.4,228.3l-4.6-0.1l-0.5-1.4l-4.8-1.1l-5.7,2.1l-7.1,2.8l-3.1,1.7l1.4,3.1l-1.2,1.6l2,2.2l1.4,3.3l-0.1,2.1 l2.3,3.9l2.4,1.9l3.7,0.6l-0.1,1.7l2.7,1.2l0.6-1.5l3.4,0.6l0.7,2l3.6,0.3l2.6,3.1l0.3,0.4l1.9-0.9l2.7,2.2l2.8-1.3l2.4,0.6l3.4-0.8 l4.9,2.3l1.1,0.4l-1.6-2.8l3.8-5.1l2.3-0.7l0.3-1.8l-3.1-5.3l-0.5-2.7l-1.9-2.9l2.7-1.2l-0.3-2.4l-1.7-2.3l-0.6-2.7l-1.4-1.9 l-2.5-0.6l-8.7,0.1L1069.4,228.3L1069.4,228.3z",
  "portugal": "M937.6,335.9l-0.4-2.1l2-2.5l0.8-1.7l-1.8-1.9l1.6-4.3l-2-3.8l2.2-0.5l0.3-3l0.9-0.9l0.2-4.9l2.4-1.7l-1.3-3.1 l-3-0.2l-0.9,0.8h-3l-1.2-3.1l-2.1,0.9l-1.9,1.6l0.1,2.1l0.9,2.2l0.1,2.7l-1.3,3.8l-0.4,2.5l-2.2,2.3l-0.6,4.2l1.2,2.4l2.3,0.6 l0.4,4l-1,5.1l2.8-0.7l2.7,0.9L937.6,335.9L937.6,335.9z",
  "san-marino": "M1040.3,293.5l-0.7,0.1l-0.2-0.9l0.9-0.3L1040.3,293.5z",
  "serbia": "M1084.8,285.2l-3.2-1.5l-0.8-1.9l-2.9-2.5l-3.2-0.2l-3.7,1.6l0,0l1.5,2.4l1.7,1.8l-1.7,2.3l0,0h1.8l-1,2.7l2.7,2.3 l-0.5,2.9l-1.2,0.3l1.5,1.1l0.8,0.8l1.8,0.7l2,1.2l-0.4,0.6l1.2-0.5l0.5-2l0.9-0.4l0.8,0.9l1,0.4l0.8,1l0.8,0.3l1.1,1.1h0.8 l-0.5,1.5l-0.5,0.7l0.2,0.5l1.7-0.4l2.4-0.1l0.7-0.9l-0.6-0.7l0.7-2l1.7-1.9l-2.8-2.6l-0.7-2.3l1.1-1.4l-1-1l1.1-1.1l-1.4-0.7 l-1.4,1.3l-3.1-1.8L1084.8,285.2L1084.8,285.2z",
  "slovakia": "M1087.4,260.9l-4.9-2.3l-3.4,0.8l-2.4-0.6l-2.8,1.3l-2.7-2.2l-1.9,0.9l-0.3-0.4h-1.5l-0.6,1.1l-1.1,0.3l-0.2,1.4 l-0.9,0.3l-0.1,0.6l-1.6,0.6l-2.2-0.1l-0.6,1.4l-0.3,0.8l0.7,2.1l2.6,1.6l1.9,0.7l4.1-0.8l0.3-1.2l1.9-0.2l2.3-1l0.6,0.4l2.2-0.7 l1-1.5l1.6-0.4l5.5,1.9l1-0.6l0.7-2.5L1087.4,260.9L1087.4,260.9z",
  "spain": "M888.3,390.4l1-0.1v0.3l-1.2,1l-0.5,1.4l-0.4,0.6l-0.3,0.2l-0.6,0.2l-0.7-0.9l-0.4-1l-0.2-0.3l0.4-0.2h0.5l1-0.1 l0.3-0.1L888.3,390.4z M883.3,392.7h-0.2l-0.2,0.2l-0.2,0.4l0.3,0.5l0.2,0.1h0.2l0.5-0.4v-0.2l-0.1-0.3L883.3,392.7z M880.6,389 l-0.3-0.4h-0.7l-0.4,0.6l0.6,1.2l0.1,0.5h0.1l0.5-0.5l0.1-0.3l-0.1-0.5l0.2-0.2L880.6,389z M878.7,395.5h-0.6l0.1,0.2l0.1,0.2 l0.7,0.4l0.6-1.1l-0.2-0.2L878.7,395.5z M901.1,389.3l-0.3,0.2l-0.1,0.6l-0.7,1.3l-0.5,1.2l-0.7,0.6l-0.7,0.2l0.1,0.1l0.7,0.1 l0.8-0.7l1.5-0.5l0.3-1l0.3-1.1v-0.7l-0.3-0.3L901.1,389.3L901.1,389.3z M893.1,393.1L893.1,393.1L893.1,393.1h-0.2l-1.3-0.1 l-0.2,0.6l-0.5,0.4v0.7l0.5,0.7l0.3,0.1l0.5,0.1l0.7-0.4l0.2-0.4l0.1-0.8l-0.1-0.4V393.1z M994.3,318.7l-0.3-0.1l-0.5,0.2l-0.5-0.2 l0.1-0.3l0.1-0.2l0.1-0.1l-0.2-0.2v-0.1l0.2-0.2l-0.2-0.1l-1.3,0.4l-0.7,0.4l-2.1,1.5v0.3l0.1,0.2h0.4l0.2,0.4l0.4-0.4l0.3-0.1 l0.3,0.1l0.3,0.2l0.1,0.6l0.1,0.2l0.6,0.1l0.9,0.4l0.4-0.2l0.5-0.3l0.2-0.6l0.3-0.5l0.3-0.5l0.3-0.4l-0.1-0.4L994.3,318.7z M998.6,317.1l-0.9-0.3l-1,0.1l-0.1,0.1v0.4l0.1,0.1l0.6,0.1l1.6,0.7h0.1l0.1-0.4v-0.1L998.6,317.1z M992,301.9l-6,0.8l-1.3-0.7 l-0.2,0.1h-0.4l-0.1-0.2v-0.2l-3.7-1.8l-1.9,1.3l-9.4-2.8l-2-2.4l-8.2-0.2l-4.2,0.3l-5.4-1h-6.8l-6.2-1.1l-7.4,4.5l2,2.6l-0.4,4.4 l1.9-1.6l2.1-0.9l1.2,3.1h3l0.9-0.8l3,0.2l1.3,3.1l-2.4,1.7l-0.2,4.9l-0.9,0.9l-0.3,3l-2.2,0.5l2,3.8l-1.6,4.3l1.8,1.9l-0.8,1.7 l-2,2.5l0.4,2.1l4.8,1l1.4,3.7l2,2.2l2.5,0.6l2.1-2.5l3.3-2.3l5,0.1h6.7l3.8-5l3.9-1.3l1.2-4.2l3-2.9l-2-3.7l2-5.1l3.1-3.5l0.5-2.1 l6.6-1.3l4.8-4.2L992,301.9z M903.7,386.3l-0.2,0.4l-0.6,0.2l-0.8,0.4l-0.2,0.3l-0.2,0.9l0.4,0.1l0.3-0.4l0.9-0.3l0.5-0.3l0.1-0.9 l0.2-0.3l-0.2-0.3L903.7,386.3z M983.7,323.1l-0.2,0.3v0.3l-0.3,0.1l-0.1,0.4l0.1,0.2l0.8,0.1l0.2-0.4h0.3l0.6-0.7v-0.3l-0.3-0.2 L983.7,323.1z M984.2,325.1l-0.1,0.2l-0.1,0.2v0.2h0.5l0.4,0.1l0.1-0.1v-0.2h-0.5L984.2,325.1z",
  "sweden": "M1077.7,161.1l-1.9-2.2l-1.7-8.4l-7.2-3.7l-5.9-2.7l-2.5,0.3v3.5l-7.9-0.9l-0.6,3.1l-4-0.1l-2.2,3.9l-3.4,6.1 l-5.7,7.9l1.8,1.9l-1.3,2.2l-4.3-0.1l-2.3,5.3l1,7.6l3.1,2.9l-0.9,6.9l-3.4,4l-1.7,3.3l4.2,8.4l4.4,6.7l2,5.7l5.3-0.3l2.2-4.7 l5.7,0.5l2-5.5l0.6-10l4.6-1.3l3.3-6.6l-4.8-3.3l-3.6-4l2.1-8.1l7.7-4.9l6.1-4.5l-1.2-3.5l3.4-3.9L1077.7,161.1L1077.7,161.1z",
  "switzerland": "M1024.3,270.6l-5.4-1.9l-1,1.4h-4.2l-1.3,1l-2.3-0.6l0.2,1.6l-3.5,3.5v2.8l2.4-0.9l1.8,2.7l2.2,1.3l2.4-0.3l2.7-2.1 l0.9,1l2.4-0.2l0.9-2.5l3.8,0.8l2.1-1.1l0.3-2.5l-2.6-0.2l-2.3-1.1l0.7-1.6L1024.3,270.6L1024.3,270.6z",
  "turkey": "M1166.6,308.9l-9.7-4.4l-8.5,0.2l-5.7,1.7l-5.6,4l-9.9-0.8l-1.6,4.8l-7.9,0.2l-5.1,6.1l3.6,3l-2,5l4.2,3.6l3.7,6.4 l5.8-0.1l5.4,3.5l3.6-0.8l0.9-2.7l5.7,0.2l4.6,3.5l8-0.7l3.1-3.7l4.6,1.5l3.2-0.6l-1.7,2.4l2.3,3l1.2-1.4l1.2-1.5l-0.1-3.6l1.9,1.3 l5.5-1.8l3,1.2h4.3l5.7-2.5l2.8,0.2l5.9-1.1l2.1-1l6.2,0.9l2.1,1.6l2.3-1.1l0,0l-3.7-5.2l0.7-2l-2.9-7.3l3.3-1.8l-2.4-1.9l-4.2-1.5 v-3.1l-1.3-2.2l-5.6-3l-5.4,0.3l-5.5,3.2l-4.5-0.6l-5.8,1L1166.6,308.9L1166.6,308.9z M1117,312.9l2-1.9l6.1-0.4l0.7-1.5l-4.7-2 l-0.9-2.4l-4.5-0.8l-5,2l2.7,1.6l-1.2,3.9l-1.1,0.7l0.1,1.3l1.9,2.9L1117,312.9L1117,312.9z",
  "uk": "M950,227.5l-4.9-3.7l-3.9,0.3l0.8,3.2l-1.1,3.2l2.9-0.1l3.5,1.3L950,227.5z M963,203.2l-5.5,0.5l-3.6-0.4l-3.7,4.8 l-1.9,6.1l2.2,3l0.1,5.8l2.6-2.8l1.4,1.6l-1.7,2.7l1,1.6l5.7,1.1h0.1l3.1,3.8l-0.8,3.5l0,0l-7.1-0.6l-1,4l2.6,3.3l-5.1,1.9l1.3,2.4 l7.5,1l0,0l-4.3,1.3l-7.3,6.5l2.5,1.2l3.5-2.3l4.5,0.7l3.3-2.9l2.2,1.2l8.3-1.7l6.5,0.1l4.3-3.3l-1.9-3.1l2.4-1.8l0.5-3.9l-5.8-1.2 l-1.3-2.3l-2.9-6.9l-3.2-1l-4.1-7.1l-0.4-0.6l-4.8-0.4l4.2-5.3l1.3-4.9h-5l-4.7,0.8L963,203.2L963,203.2z",
  "belize": "M504.8,401.5L504.7,400.6L505.4,400.4L506.4,401.1L508.4,397.7L509.4,397.6L509.5,398.4L510.5,398.5L510.4,400.0L509.5,402.4L510.0,403.2L509.4,405.2L509.8,405.8L509.1,408.6L508.0,410.0L507.0,410.2L505.9,412.2L504.3,412.2L504.7,405.9L504.8,401.5Z",
  "canada": "M317.6,228.0L316.8,228.0L306.1,222.5L302.1,220.1L292.0,217.8L288.9,212.9L289.7,209.5L282.6,207.1L281.6,202.6L274.9,198.6L274.8,195.7L277.9,193.1L277.7,189.5L268.3,186.0L262.6,179.7L259.1,175.7L254.0,173.2L250.3,170.9L247.4,168.0L241.8,169.8L236.4,172.9L231.4,169.3L227.6,166.8L222.1,165.3L216.7,165.1L216.7,133.5L216.7,112.8L227.1,114.2L235.9,116.8L241.6,117.4L246.5,115.0L253.2,113.3L261.5,114.0L269.8,111.5L278.9,110.1L282.7,112.4L286.9,111.1L288.1,108.5L292.0,109.1L301.4,114.1L308.7,110.3L309.5,114.6L316.3,113.7L318.4,112.0L325.2,112.3L333.6,114.7L346.6,116.7L354.3,117.7L359.7,117.3L367.2,120.1L359.4,122.9L369.5,124.1L384.5,123.4L389.2,122.5L395.1,125.8L401.1,123.0L395.5,120.6L399.1,118.7L405.8,118.5L410.3,117.9L414.8,119.2L420.3,122.2L426.5,121.8L436.4,124.3L445.0,123.4L453.1,123.6L452.4,120.1L457.4,119.1L466.0,121.0L466.0,126.3L469.5,121.8L474.0,122.0L476.5,116.4L470.5,113.0L464.0,110.7L464.5,104.6L471.1,100.5L478.4,101.4L484.0,103.9L491.6,110.2L486.6,112.9L497.0,114.0L496.9,119.7L504.4,115.3L511.0,118.9L509.3,123.0L514.7,126.8L520.5,122.8L524.6,118.0L524.9,111.9L532.8,112.3L541.0,113.1L548.4,115.9L548.8,118.6L544.6,121.6L548.6,124.6L547.8,127.3L537.0,131.2L529.2,132.0L523.5,130.4L521.8,133.2L516.5,137.8L514.9,140.3L508.4,144.0L500.5,144.4L496.1,146.8L495.7,150.4L489.3,151.1L482.5,155.6L476.4,161.8L474.3,166.2L474.0,172.7L482.1,173.6L484.6,178.8L487.2,183.0L495.0,181.9L505.3,184.3L510.9,186.5L514.9,189.1L521.8,190.6L527.7,193.0L536.9,193.3L542.9,193.8L542.0,198.6L543.7,204.2L547.8,210.4L556.0,215.7L560.3,213.9L563.3,208.2L560.4,199.4L556.5,196.5L565.4,193.9L571.7,190.0L574.8,186.1L574.3,182.4L570.5,177.7L563.8,173.5L570.3,167.7L567.9,162.6L566.1,153.9L569.9,152.6L579.5,154.2L585.2,154.7L589.8,153.2L594.9,155.1L601.8,158.4L603.5,160.5L613.4,160.9L613.2,165.6L615.1,172.6L620.1,173.5L624.2,176.8L632.2,173.7L637.5,167.5L641.2,165.0L645.5,169.9L652.8,177.0L658.9,183.7L656.7,187.2L664.1,190.3L669.1,193.5L677.9,194.9L681.5,196.7L683.7,201.4L688.0,202.2L690.2,204.3L690.6,210.5L686.6,212.6L682.6,214.5L673.5,216.5L666.5,221.1L657.1,222.0L645.2,220.8L636.9,220.8L631.1,221.2L626.5,225.2L619.4,227.6L611.4,235.0L605.0,240.1L609.7,239.2L618.6,231.9L630.3,227.3L638.6,226.7L643.5,229.4L638.2,233.2L640.0,239.2L641.8,243.4L649.0,246.1L658.2,245.3L663.8,239.1L664.2,243.1L667.8,245.1L660.9,248.8L648.6,252.1L643.1,254.3L636.9,258.3L632.6,257.9L632.4,253.2L642.1,248.6L633.2,248.8L627.0,249.5L623.4,246.3L623.4,238.8L620.9,237.2L617.2,238.1L615.3,236.6L611.1,240.8L609.4,245.2L607.4,247.7L605.1,248.6L603.3,248.8L602.7,250.2L592.5,250.2L584.1,250.2L581.6,251.3L575.7,255.3L575.0,255.7L573.2,257.9L568.1,257.9L562.7,257.9L560.2,258.8L561.0,259.9L561.5,261.6L561.4,262.1L554.2,264.9L548.5,265.8L542.0,268.7L540.6,268.7L538.7,267.9L538.1,267.1L538.2,266.5L539.4,264.5L542.1,261.5L543.7,258.2L542.6,253.4L541.4,248.3L535.6,245.7L536.3,244.7L535.5,244.0L533.9,244.0L532.8,243.2L532.5,241.8L531.5,242.4L530.0,242.2L530.3,241.7L529.0,241.1L528.5,239.7L524.1,237.9L519.7,236.1L514.2,233.9L509.0,231.9L504.0,233.5L502.2,233.5L495.4,232.1L490.9,232.8L485.5,231.1L479.8,230.2L475.9,229.8L474.2,228.9L473.2,225.8L471.4,225.9L471.3,228.0L459.8,228.0L440.8,228.0L421.9,228.0L405.3,228.0L388.6,228.0L372.2,228.0L355.3,228.0L349.8,228.0L333.3,228.0L317.6,228.0ZM533.4,153.2L537.5,150.6L545.1,150.7L545.0,151.8L538.5,154.8L534.6,154.7L533.4,153.2ZM556.8,95.6L550.7,92.7L550.9,90.7L553.6,90.3L566.3,90.9L575.9,94.0L576.4,95.5L570.5,95.3L564.5,95.2L558.4,96.0L556.8,95.6ZM553.8,155.2L555.9,153.6L558.2,153.7L559.6,154.8L557.5,157.7L555.0,157.3L553.5,155.6L553.8,155.2ZM479.9,83.5L476.9,85.7L468.8,85.3L462.1,83.8L465.1,81.3L473.0,79.8L477.9,81.8L479.9,83.5ZM478.7,69.4L476.1,69.6L465.7,69.2L464.2,67.7L475.4,67.7L479.3,68.8L478.7,69.4ZM462.5,62.5L469.1,64.4L467.6,66.4L459.4,67.6L454.9,66.3L452.5,64.2L452.0,61.9L459.2,62.1L462.5,62.5ZM510.3,86.8L501.3,86.1L486.5,84.3L484.6,81.3L483.9,78.5L478.4,76.1L466.9,75.4L460.4,73.7L462.5,71.4L474.0,71.7L480.1,73.5L491.1,73.5L495.9,75.4L494.6,77.4L501.0,78.7L504.5,80.0L512.0,80.3L520.1,80.7L528.9,79.5L540.3,79.1L549.3,79.4L555.2,81.5L556.5,83.8L553.0,85.3L544.7,86.5L537.6,85.8L521.7,86.7L510.3,86.8ZM381.9,65.9L389.7,66.7L387.8,68.4L377.5,70.0L369.3,68.2L373.7,66.4L381.9,65.9ZM383.5,62.3L390.8,63.4L384.0,64.5L374.8,64.5L374.9,63.7L380.6,62.0L383.5,62.3ZM691.1,215.1L688.1,218.6L684.5,223.5L688.1,221.6L691.8,222.8L689.9,224.7L694.8,226.3L697.4,224.9L702.9,226.6L701.2,230.7L705.1,229.7L705.8,232.7L707.5,236.1L705.2,241.0L702.7,241.2L699.0,240.2L700.2,235.6L698.7,234.9L692.2,239.8L688.9,239.6L692.8,237.0L687.5,235.6L681.5,235.9L670.7,235.8L669.9,234.1L673.3,232.2L670.9,230.7L675.6,227.3L681.3,218.5L684.8,215.3L689.6,213.4L692.2,213.6L691.1,215.1ZM534.0,138.4L540.1,140.3L546.4,142.1L546.9,144.7L551.0,144.3L555.0,146.1L550.0,147.9L541.4,146.5L538.3,144.0L532.8,147.0L524.9,149.9L523.0,146.6L515.4,147.1L520.3,144.4L521.0,140.0L522.9,134.9L526.9,135.4L527.9,137.8L530.8,137.0L534.0,138.4ZM562.4,98.1L567.6,95.9L580.0,98.7L587.6,101.4L588.3,103.8L598.6,102.6L604.4,106.1L617.8,108.3L622.7,110.5L627.9,115.8L617.7,118.3L630.8,122.0L639.6,123.2L647.6,128.3L656.4,128.7L654.6,132.6L644.9,139.0L638.1,136.7L629.3,131.3L622.1,132.0L621.4,135.2L627.3,138.4L634.8,141.0L637.1,142.5L640.7,148.0L638.8,152.0L631.8,150.5L617.9,146.0L625.7,150.8L631.5,154.2L632.4,156.1L617.3,153.9L605.4,150.6L598.7,147.9L600.6,146.4L592.3,143.5L584.2,140.8L584.3,142.4L568.3,143.3L563.6,141.4L567.2,137.3L577.7,137.2L589.1,136.5L587.3,134.5L589.2,131.7L596.4,126.3L594.8,123.9L592.7,122.0L584.2,119.3L572.9,117.4L576.5,116.0L570.6,112.5L565.7,112.2L561.3,110.3L558.4,111.9L548.3,112.7L528.1,111.4L516.3,109.8L507.3,108.9L502.7,107.0L508.5,104.4L500.6,104.4L498.9,98.8L503.1,93.8L508.8,91.6L523.2,90.1L519.1,93.7L523.5,97.1L528.6,92.6L542.7,90.4L552.2,96.1L551.4,99.8L562.4,98.1ZM475.0,88.2L486.6,88.4L497.2,89.8L488.9,94.7L482.2,95.8L476.3,100.0L469.9,99.8L466.5,94.9L466.6,92.1L469.5,89.7L475.0,88.2ZM317.5,77.2L326.9,73.0L338.3,69.4L346.8,69.5L354.4,68.7L353.7,73.0L349.4,74.9L344.2,75.2L333.9,77.6L325.0,78.4L317.5,77.2ZM262.7,200.0L268.1,199.5L266.4,205.8L271.2,210.3L269.0,210.3L265.7,207.8L263.6,205.2L260.8,203.5L259.8,201.0L260.1,199.3L262.7,200.0ZM413.9,59.5L424.8,60.3L439.9,62.3L444.1,64.9L446.3,67.2L437.2,66.6L428.1,64.8L415.7,64.6L421.0,63.0L414.3,61.6L413.9,59.5ZM313.8,230.7L311.0,231.5L301.9,229.0L300.2,227.0L295.3,225.1L294.3,223.5L288.6,222.5L286.4,219.4L286.9,218.2L292.7,219.4L296.1,220.2L301.4,220.8L303.2,222.7L306.0,225.4L311.5,227.7L313.8,230.7ZM324.8,86.5L332.7,87.6L346.9,87.9L352.3,89.6L358.3,91.9L351.3,93.3L337.7,97.2L330.8,101.1L330.8,103.5L316.2,106.2L313.2,103.8L300.4,100.8L302.8,98.5L306.6,94.4L311.4,90.8L306.0,87.4L324.8,86.5ZM401.0,78.7L405.9,77.8L411.8,78.0L412.7,80.7L409.4,83.4L390.6,84.2L376.5,86.7L368.1,86.8L367.4,85.0L378.9,82.5L353.8,83.2L346.0,82.2L353.6,76.7L358.9,75.2L374.5,77.1L384.4,80.4L394.1,80.8L386.1,75.5L391.2,73.4L396.9,74.1L398.8,76.7L401.0,78.7ZM408.2,94.1L414.4,96.4L417.9,101.8L419.6,105.7L429.0,108.5L439.0,111.1L438.4,113.5L429.3,114.0L432.8,116.1L430.9,118.2L420.9,117.3L411.3,115.8L404.9,116.1L394.4,118.0L380.4,118.8L370.5,119.4L367.5,116.7L359.9,115.2L355.0,115.8L348.1,111.4L351.8,110.9L360.4,109.9L368.2,110.2L375.5,109.2L364.7,107.9L352.8,108.3L345.0,108.2L342.0,106.2L354.9,103.9L346.4,104.0L336.7,102.6L341.3,98.4L345.2,96.2L360.1,92.8L365.7,93.9L363.0,96.5L375.3,94.8L383.0,97.6L389.3,94.8L394.4,96.6L398.9,102.0L401.7,99.7L397.8,94.0L402.7,93.2L408.2,94.1ZM442.0,96.2L435.9,92.5L442.5,89.8L449.1,91.0L459.0,90.3L460.4,91.9L455.3,94.6L463.7,97.0L462.7,102.0L453.6,104.1L448.2,103.7L444.4,101.6L430.6,97.3L430.7,95.5L442.0,96.2ZM407.8,91.2L415.2,91.0L419.4,92.2L414.6,95.9L405.9,92.0L407.8,91.2ZM452.8,73.9L457.0,76.4L457.2,79.3L454.7,83.4L445.5,84.0L439.5,83.1L439.6,79.9L430.5,80.3L430.2,76.0L436.2,76.2L444.5,74.3L452.3,74.6L452.8,73.9ZM466.6,52.3L470.4,50.6L476.1,50.2L473.7,48.9L486.6,48.6L493.7,51.6L503.1,52.8L512.2,53.8L516.6,57.5L523.2,59.3L515.6,61.0L505.4,65.1L495.5,65.5L484.0,64.8L478.0,62.6L478.1,60.5L482.5,59.1L472.4,59.1L466.2,57.3L462.7,54.7L466.6,52.3ZM491.2,45.1L499.4,44.0L505.9,43.8L516.8,42.9L525.0,40.9L531.9,41.1L537.9,42.7L542.1,39.7L549.4,38.8L559.4,38.2L576.4,38.0L579.3,38.6L595.4,37.6L607.4,38.0L619.4,38.3L634.3,38.8L646.2,39.5L656.4,41.0L656.1,42.5L642.6,44.9L629.1,46.0L624.1,47.3L636.2,47.2L623.1,50.6L614.1,52.2L604.5,56.7L593.1,57.6L589.5,58.8L572.7,59.4L580.4,60.1L576.5,61.1L581.1,63.8L575.9,65.7L567.3,67.3L564.6,69.5L556.9,71.1L557.7,72.4L567.2,72.2L567.3,73.5L552.4,76.9L536.3,75.3L520.0,76.2L511.7,75.5L501.2,75.2L500.5,72.6L510.8,71.3L508.1,67.3L511.5,66.9L526.3,69.3L518.7,65.7L509.7,64.7L514.2,62.5L524.1,61.2L525.6,59.2L517.8,57.1L515.4,54.2L530.6,54.5L535.0,55.1L543.7,53.0L531.2,52.4L511.7,52.7L501.9,50.9L497.3,48.6L490.8,47.0L489.6,45.1ZM582.1,125.4L578.5,127.1L572.3,127.4L570.9,124.6L573.3,121.5L578.4,120.7L582.7,122.3L582.8,124.7L582.1,125.4ZM465.2,114.1L468.6,116.2L465.2,118.1L457.7,116.4L453.2,117.1L445.6,114.6L450.5,112.8L454.3,110.4L460.2,112.0L463.6,113.0L465.2,114.1ZM641.6,223.1L643.5,222.7L650.8,224.1L656.5,226.4L656.6,227.4L653.9,227.5L646.7,225.8L641.6,223.1ZM644.4,238.9L646.3,241.6L650.3,242.4L655.5,242.2L652.7,244.5L650.7,244.9L643.6,242.5L642.3,240.6L644.4,238.9Z",
  "costa-rica": "M541.4,447.3L539.3,447.8L539.3,450.0L540.4,450.9L539.6,451.5L539.8,452.5L539.4,453.7L539.1,454.8L536.1,453.5L534.9,452.4L535.6,451.4L535.4,450.2L533.8,448.8L531.6,447.7L529.7,447.0L529.4,445.4L527.9,444.4L528.3,446.0L527.2,447.4L525.9,445.8L524.1,445.3L523.3,444.1L523.4,442.4L524.1,440.7L522.5,439.9L523.8,438.8L524.7,438.1L528.3,439.6L529.6,438.9L531.4,439.3L532.3,440.5L533.9,440.8L535.2,439.7L536.6,442.7L538.8,444.9L541.4,447.3Z",
  "mexico": "M349.3,319.6L355.6,319.1L362.7,318.5L362.1,319.6L370.5,322.3L383.2,326.2L394.2,326.2L398.7,326.2L398.7,323.9L408.3,323.9L410.3,325.9L413.2,327.6L416.5,330.1L418.3,333.0L419.7,336.1L422.6,337.7L427.2,339.4L430.7,335.0L435.2,334.9L439.1,337.1L441.9,340.9L443.8,344.2L447.1,347.3L448.3,351.2L449.9,353.8L454.2,355.6L458.2,356.8L460.3,356.6L458.2,361.5L457.2,365.5L456.8,373.0L456.3,375.7L457.2,378.7L458.9,381.4L460.1,385.7L463.7,389.9L465.0,393.1L467.2,395.8L473.1,397.3L475.4,399.6L480.3,398.0L484.5,397.5L488.7,396.5L492.2,395.5L495.7,393.3L497.0,390.0L497.5,385.3L498.4,383.7L502.2,382.3L508.1,381.0L513.0,381.2L516.4,380.7L517.7,381.9L517.5,384.6L514.5,387.9L513.2,391.2L514.2,392.2L513.4,394.6L512.0,399.0L510.6,397.5L509.4,397.6L508.4,397.7L506.4,401.1L505.4,400.4L504.7,400.6L504.8,401.5L499.6,401.4L494.4,401.4L494.4,404.5L491.9,404.6L494.0,406.4L496.0,407.7L496.7,408.9L497.6,409.2L497.4,411.1L490.3,411.2L487.6,415.7L488.4,416.7L487.8,418.0L487.6,419.6L481.3,413.7L478.5,411.9L473.9,410.4L470.8,410.8L466.4,412.9L463.6,413.4L459.6,412.0L455.5,410.9L450.3,408.4L445.6,405.7L444.2,404.2L441.1,403.9L435.4,402.1L433.1,399.6L427.1,396.5L424.4,392.9L423.0,390.2L424.9,389.7L424.3,388.1L425.6,386.7L425.6,384.7L423.8,382.2L423.3,380.0L421.4,377.2L416.5,371.7L410.9,367.3L408.2,363.9L403.4,361.6L402.4,360.3L403.3,356.8L400.4,355.5L397.1,352.8L395.8,348.9L392.8,348.5L389.5,345.6L386.9,342.8L386.7,341.1L383.7,336.9L381.7,332.7L381.8,330.5L377.8,328.3L376.0,328.6L372.8,327.0L371.9,329.3L372.8,332.0L373.4,336.1L375.3,338.4L379.4,342.3L380.3,343.6L381.1,344.0L381.9,345.9L382.9,345.8L384.0,349.4L385.7,350.8L386.9,352.8L390.3,355.6L392.2,360.8L393.8,363.2L395.4,365.8L395.7,368.7L398.4,368.9L400.6,371.5L402.6,373.9L402.5,374.9L400.1,377.0L399.2,376.9L397.7,373.6L394.1,370.4L390.0,367.7L387.2,366.3L387.4,362.2L386.5,359.2L383.9,357.5L380.1,355.0L379.3,355.7L377.9,354.3L374.5,352.9L371.2,349.7L371.6,349.3L373.9,349.6L376.0,347.5L376.2,345.0L371.9,341.0L368.7,339.5L366.6,336.0L364.6,332.4L362.0,327.9L359.7,322.9Z",
  "panama": "M570.3,452.3L569.6,453.1L570.9,456.4L569.8,458.0L568.0,457.6L567.3,460.3L565.5,458.7L564.3,455.7L565.6,454.2L564.2,453.9L563.2,452.0L560.4,450.5L558.0,450.8L556.9,452.8L554.6,454.2L553.4,454.3L552.9,455.5L555.5,458.5L554.0,459.2L553.2,460.1L550.6,460.3L549.7,457.0L548.9,458.0L547.1,457.6L546.0,455.4L543.7,455.0L542.3,454.4L539.9,454.4L539.7,455.6L539.1,454.8L539.4,453.7L539.8,452.5L539.6,451.5L540.4,450.9L539.3,450.0L539.3,447.8L541.4,447.3L543.4,449.3L543.3,450.5L545.5,450.7L546.0,450.3L547.6,451.6L550.3,451.2L552.7,449.8L556.0,448.7L557.9,447.1L561.0,447.4L560.8,447.9L563.9,448.1L566.4,449.1L568.2,450.7L570.3,452.3Z",
  "usa": "M317.6,228.0L333.3,228.0L349.8,228.0L355.3,228.0L372.2,228.0L388.6,228.0L405.3,228.0L421.9,228.0L440.8,228.0L459.8,228.0L471.3,228.0L471.4,225.9L473.2,225.8L474.2,228.9L475.9,229.8L479.8,230.2L485.5,231.1L490.9,232.8L495.4,232.1L502.2,233.5L504.0,233.5L509.0,231.9L514.2,233.9L519.7,236.1L524.1,237.9L528.5,239.7L529.0,241.1L530.3,241.7L530.0,242.2L531.5,242.4L532.5,241.8L532.8,243.2L533.9,244.0L535.5,244.0L536.3,244.7L535.6,245.7L541.4,248.3L542.6,253.4L543.7,258.2L542.1,261.5L539.4,264.5L538.2,266.5L538.1,267.1L538.7,267.9L540.6,268.7L542.0,268.7L548.5,265.8L554.2,264.9L561.4,262.1L561.5,261.6L561.0,259.9L560.2,258.8L562.7,257.9L568.1,257.9L573.2,257.9L575.0,255.7L575.7,255.3L581.6,251.3L584.1,250.2L592.5,250.2L602.7,250.2L603.3,248.8L605.1,248.6L607.4,247.7L609.4,245.2L611.1,240.8L615.3,236.6L617.2,238.1L620.9,237.2L623.4,238.8L623.4,246.3L627.0,249.5L628.0,251.3L622.0,254.0L616.3,255.9L610.5,257.6L607.5,260.9L606.6,262.1L606.5,265.1L608.4,268.0L610.7,268.2L610.1,266.1L611.7,267.4L611.3,268.9L607.5,269.9L604.9,269.7L600.8,270.7L598.4,271.0L595.1,271.3L590.5,272.9L598.7,271.8L600.3,272.9L592.5,274.5L589.0,274.6L589.1,273.9L587.5,275.4L589.1,275.7L587.9,279.7L583.8,284.0L583.4,282.5L582.2,282.2L580.4,280.8L581.5,283.8L582.9,284.8L583.0,286.9L581.2,289.1L578.1,293.5L577.6,293.3L579.3,289.5L576.5,287.4L575.8,282.8L574.8,285.2L575.9,288.7L572.3,287.8L576.1,289.6L576.3,294.9L577.9,295.3L578.5,297.2L579.3,302.8L575.8,306.9L570.0,308.6L566.4,311.8L563.6,312.2L560.8,314.2L560.0,316.1L553.9,319.7L550.7,322.4L548.1,325.7L547.3,329.6L548.3,333.5L550.1,338.2L552.6,342.2L552.6,344.6L555.2,351.0L555.1,354.8L554.8,356.9L553.4,360.3L551.8,361.0L549.0,360.4L548.2,357.9L546.1,356.6L543.1,351.9L540.5,347.6L539.7,345.4L540.8,341.7L539.3,338.7L534.9,334.0L532.8,333.2L527.2,335.7L526.2,335.4L523.5,332.8L520.0,331.4L513.7,332.1L508.8,331.5L504.5,331.9L502.3,332.8L503.3,334.3L503.2,336.5L504.3,337.6L503.3,338.3L501.2,337.5L499.1,338.6L495.1,338.4L491.0,335.5L486.1,336.2L482.1,334.9L478.6,335.3L473.9,336.6L468.9,340.7L463.4,343.1L460.3,345.7L459.1,348.2L459.0,352.1L459.3,354.7L460.3,356.6L458.2,356.8L454.2,355.6L449.9,353.8L448.3,351.2L447.1,347.3L443.8,344.2L441.9,340.9L439.1,337.1L435.2,334.9L430.7,335.0L427.2,339.4L422.6,337.7L419.7,336.1L418.3,333.0L416.5,330.1L413.2,327.6L410.3,325.9L408.3,323.9L398.7,323.9L398.7,326.2L394.2,326.2L383.2,326.2L370.5,322.3L362.1,319.6L362.7,318.5L355.6,319.1L349.3,319.6L348.4,316.7L344.8,313.5L342.2,312.9L341.6,311.3L338.4,311.0L336.4,309.5L331.3,308.9L329.9,308.0L329.2,305.0L323.8,299.4L319.2,291.7L319.4,290.4L316.9,288.5L312.6,283.9L311.9,279.3L308.9,276.3L310.1,271.7L309.9,266.9L308.1,262.7L310.3,257.4L311.0,252.4L311.7,247.3L310.7,239.9L308.9,235.1L307.3,232.5L308.0,231.5L316.0,233.3L319.0,238.6L320.3,237.1L319.4,232.6L317.6,228.0ZM136.7,388.8L137.6,389.3L138.5,390.1L140.0,392.0L139.8,392.3L137.7,393.5L135.9,394.4L135.1,395.3L133.7,394.5L133.8,393.0L132.9,390.9L133.2,390.3L134.2,389.4L133.8,388.3L134.1,387.8L134.5,387.9L136.7,388.8ZM133.4,385.0L132.9,385.7L131.0,386.1L130.1,384.9L129.4,384.5L129.4,384.1L129.9,383.6L131.9,384.2L133.4,385.0ZM129.1,382.7L128.9,383.3L126.0,383.2L126.4,382.5L129.1,382.7ZM122.1,379.7L122.5,380.1L124.1,381.9L123.8,382.2L123.5,382.2L121.5,382.0L120.8,380.7L120.6,380.5L122.1,379.7ZM114.6,377.0L114.7,378.3L114.1,378.8L112.2,377.8L112.5,377.4L113.4,376.8L114.6,377.0ZM75.2,164.7L79.6,165.2L80.1,167.3L76.7,168.2L73.1,167.2L69.7,165.6L75.2,164.7ZM148.7,178.1L152.4,178.5L154.8,180.2L150.0,182.9L144.4,185.0L141.6,183.6L140.7,181.0L145.8,179.0L148.7,178.1ZM216.7,112.8L216.7,133.5L216.7,165.1L222.1,165.3L227.6,166.8L231.4,169.3L236.4,172.9L241.8,169.8L247.4,168.0L250.3,170.9L254.0,173.2L259.1,175.7L262.6,179.7L268.3,186.0L277.7,189.5L277.9,193.1L274.8,195.7L271.7,193.6L266.8,191.9L265.3,187.0L258.1,182.5L255.1,177.3L249.8,176.9L241.0,176.8L234.4,175.2L223.0,169.4L217.6,168.3L207.9,166.4L200.2,166.8L189.3,164.3L182.7,161.9L176.5,163.1L177.7,167.0L174.6,167.3L168.2,168.5L163.3,170.3L157.1,171.5L156.3,168.3L158.8,162.8L164.7,161.1L163.2,159.7L156.1,162.8L152.3,166.5L144.3,170.4L148.4,173.1L143.2,177.1L137.2,179.5L131.6,181.2L130.2,183.6L121.6,186.5L119.8,189.1L113.3,191.5L109.5,191.1L104.3,192.6L98.7,194.5L94.1,196.4L84.5,198.0L83.7,197.0L89.7,194.4L95.2,192.7L101.1,189.7L108.0,189.0L110.7,186.7L118.4,183.4L119.7,182.3L123.8,180.3L124.7,176.1L127.5,172.8L121.1,174.5L119.3,173.6L116.3,175.6L112.7,172.8L111.2,174.8L109.1,172.0L103.6,174.2L100.2,174.2L99.7,170.9L100.7,168.9L97.1,166.9L89.9,168.0L85.2,165.3L81.4,164.0L81.4,160.9L77.1,158.5L79.3,155.3L83.8,152.2L85.8,149.3L90.3,148.9L94.1,149.8L98.6,147.1L102.6,147.6L106.8,145.9L105.8,143.3L102.7,142.4L106.8,140.2L103.4,140.3L97.5,141.5L95.8,142.7L91.4,141.5L83.6,142.1L75.4,140.8L73.1,138.5L66.1,135.3L73.9,133.0L86.3,130.3L90.8,130.3L90.1,133.0L101.8,132.8L97.3,129.4L90.4,127.3L86.5,124.5L81.2,122.1L73.5,120.3L76.6,117.4L86.5,117.3L93.5,114.7L94.8,112.0L100.5,109.4L105.9,108.7L116.4,106.3L121.6,106.6L130.1,103.7L138.5,104.8L142.5,107.3L145.0,106.3L154.4,106.6L154.1,107.9L162.6,108.8L168.2,108.3L179.9,110.0L190.6,110.6L194.9,111.3L202.3,110.4L210.7,112.0L216.7,112.8ZM45.9,145.8L49.4,146.9L52.8,146.3L57.3,147.8L62.8,148.5L62.4,149.1L58.2,150.3L53.9,149.1L51.8,148.1L46.9,148.4L45.6,147.9L45.9,145.8Z",
  "argentina": "M669.8,920.7l0.9-3l-7.3-1.5l-7.7-3.6l-4.3-4.6l-3-2.8l5.9,13.5h5l2.9,0.2l3.3,2.1L669.8,920.7L669.8,920.7z M619.4,712.6l-7.4-1.5l-4,5.7l0.9,1.6l-1.1,6.6l-5.6,3.2l1.6,10.6l-0.9,2l2,2.5l-3.2,4l-2.6,5.9l-0.9,5.8l1.7,6.2l-2.1,6.5 l4.9,10.9l1.6,1.2l1.3,5.9l-1.6,6.2l1.4,5.4l-2.9,4.3l1.5,5.9l3.3,6.3l-2.5,2.4l0.3,5.7l0.7,6.4l3.3,7.6l-1.6,1.2l3.6,7.1l3.1,2.3 l-0.8,2.6l2.8,1.3l1.3,2.3l-1.8,1.1l1.8,3.7l1.1,8.2l-0.7,5.3l1.8,3.2l-0.1,3.9l-2.7,2.7l3.1,6.6l2.6,2.2l3.1-0.4l1.8,4.6l3.5,3.6 l12,0.8l4.8,0.9l2.2,0.4l-4.7-3.6l-4.1-6.3l0.9-2.9l3.5-2.5l0.5-7.2l4.7-3.5l-0.2-5.6l-5.2-1.3l-6.4-4.5l-0.1-4.7l2.9-3.1l4.7-0.1 l0.2-3.3l-1.2-6.1l2.9-3.9l4.1-1.9l-2.5-3.2l-2.2,2l-4-1.9l-2.5-6.2l1.5-1.6l5.6,2.3l5-0.9l2.5-2.2l-1.8-3.1l-0.1-4.8l-2-3.8 l5.8,0.6l10.2-1.3l6.9-3.4l3.3-8.3l-0.3-3.2l-3.9-2.8l-0.1-4.5l-7.8-5.5l-0.3-3.3l-0.4-4.2l0.9-1.4l-1.1-6.3l0.3-6.5l0.5-5.1 l5.9-8.6l5.3-6.2l3.3-2.6l4.2-3.5l-0.5-5.1l-3.1-3.7l-2.6,1.2l-0.3,5.7l-4.3,4.8l-4.2,1.1l-6.2-1l-5.7-1.8l4.2-9.6l-1.1-2.8 l-5.9-2.5l-7.2-4.7l-4.6-1L632,713.7l-1-1.3l-6.3-0.3l-1.6,5.1L619.4,712.6L619.4,712.6z",
  "bolivia": "M655.7,700.5l1.6-1.3l-0.8-3.6l1.3-2.8l0.5-5l-1.6-4l-3.2-1.7l-0.8-2.6l0.6-3.6l-10.7-0.3l-2.7-7.4l1.6-0.1 l-0.3-2.8l-1.2-1.8l-0.5-3.7l-3.3-1.9l-3.5,0.1l-2.5-1.9l-3.8-1.2l-2.4-2.4l-6.3-1l-6.4-5.7l0.3-4.3l-0.9-2.5l0.4-4.7l-7.3,1.1 l-2.8,2.3l-4.8,2.6l-1.1,1.9l-2.9,0.2l-4.2-0.6l5.5,10.3l-1.1,2.1l0.1,4.5l0.3,5.4l-1.9,3.2l1.2,2.4l-1.1,2.1l2.8,5.3L591,684 l3.1,4.3l1.2,4.6l3.2,2.7l-1.1,6.2l3.7,7.1l3.1,8.8l3.8-0.9l4-5.7l7.4,1.5l3.7,4.6l1.6-5.1l6.3,0.3l1,1.3l1.5-7.6l-0.2-3.4l2.1-5.6 l9.5-1.9l5.1,0.1l5.4,3.3L655.7,700.5L655.7,700.5z",
  "brazil": "M659,560.1l-1.4,0.2l-3.1-0.5l-1.8,1.7l-2.6,1.1l-1.7,0.2l-0.7,1.3l-2.7-0.3l-3.5-3l-0.3-2.9l-1.4-3.3l1-5.4 l1.6-2.2l-1.2-3l-1.9-0.9l0.8-2.8l-1.3-1.5l-2.9,0.3l0.7,1.8l-2.1,2.4l-6.4,2.4l-4,1l-1.7,1.5l-4.4-1.6l-4.2-0.8l-1,0.6l2.4,1.6 l-0.3,4.3l0.7,4l4.8,0.5l0.3,1.4l-4.1,1.8l-0.7,2.7l-2.3,1l-4.2,1.5l-1.1,1.9l-4.4,0.5l-3-3.4l-1.1,0.8l-1-3.8l-1.6-2l-1.9,2.2 l-10.9-0.1v3.9l3.3,0.7l-0.2,2.4l-1.1-0.6l-3.2,1v4.6l2.5,2.4l0.9,3.6l-0.1,2.8l-2.2,17.4l-5.1-0.3l-0.7,1l-4.6,1.2l-6.2,4.3l-0.4,3 l-1.3,2.2l0.7,3.4l-3.3,1.9l0.1,2.7L562,620l2.6,5.8l3.3,3.8l-1,2.8l3.7,0.3l2.3,3.4l4.9,0.2l4.4-3.8l0.2,9.7l2.6,0.7l3-1.1l4.2,0.6 l2.9-0.2l1.1-1.9l4.8-2.6l2.8-2.3l7.3-1.1l-0.4,4.7l0.9,2.5l-0.3,4.3l6.4,5.7l6.3,1l2.4,2.4l3.8,1.2l2.5,1.9l3.5-0.1l3.3,1.9 l0.5,3.7l1.2,1.8l0.3,2.8l-1.6,0.1l2.7,7.4l10.7,0.3l-0.6,3.6l0.8,2.6l3.2,1.7l1.6,4l-0.5,5l-1.3,2.8l0.8,3.6l-1.6,1.3l1.9,3.6 l0.4,8.6l6,1.2l2.1-1.2l3.9,1.7l1.2,1.9l1,5.8l0.9,2.5l2,0.3l2-1.1l2.1,1.2l0.3,3.5l-0.3,3.8l-0.7,3.6l2.6-1.2l3.1,3.7l0.5,5.1 l-4.2,3.5l-3.3,2.6l-5.3,6.2l-5.9,8.6l3.4-0.7l6.2,4.9l1.9-0.2l6.2,4.1l4.8,3.5l3.8,4.3l-1.9,3l2.1,3.7l2.9-3.7l1.5-6l3.2-3l3.9-5 l4.5-11.2l3.4-3.5l0.8-3.1l0.3-6.4l-1.3-3.5l0.3-4.8l4.1-6.3l6-5.1l6-1.8l3.6-2.9l8.5-2.4h5.9l1.1-3.8l4.2-2.8l0.6-6.5l5.1-8.3 l0.5-8.5l1.6-2.6l0.3-4.1l1.1-9.9l-1-11.9l1.4-4.7l1.4-0.1l3.9-5.5l3.3-7.2l7.7-8.8l2.7-4.2l2-10.5l-1-3.9l-2-8.1l-2.1-2l-4.8-0.2 l-4.3-1.9l-7.3-7.1l-8.4-5.3l-8.4,0.3l-10.9-3.4l-6.5,2l0.8-3.5l-2.7-3.8l-9.4-3.8l-7.1-2.3l-4.2,4.1l-0.3-6.3l-9.9-1l-1.7-2 l4.2-5.2l-0.1-4.4l-3-1l-3-11.2l-1.3-3.5l-1.9,0.3l-3.5,5.8l-1.8,4.7l-2.1,2.4l-2.7,0.5l-0.8-1.8l-1.2-0.3l-1.8,1.8l-2.4-1.3 l-3.2-1.4l-2.7,0.7l-2.3-0.6l-0.5,1.8l0.9,1.3l-0.5,1.3L659,560.1L659,560.1z",
  "chile": "M648.4,905.2l-3.7-0.7l-3.3,2.5l0.2,4.1l-1.2,2.8l-7.2-2.2l-8.6-4l-4.5-1.3l9.7,6.8l6.3,3.2l7.5,3.4l5.3,0.9 l4.3,1.8l3,0.5l2.3,0.1l3.2-1.8l0.5-2.4l-2.9-0.2h-5L648.4,905.2L648.4,905.2z M601.1,708.9l-3.7-7.1l1.1-6.2l-3.2-2.7l-1.2-4.6 L591,684l-1.2,3.3l-2.7,1.6l2.1,9l1.5,10.4l-0.1,14.2v13.2l0.9,12.3l-1.9,7.8l2.1,7.8l-0.5,5.3l3.2,9.5l-0.1,9.5l-1.2,10.2 l-0.6,10.5l-2.1,0.2l2.4,7.3l3.3,6.3l-1.1,4.3l1.9,11.6l1.5,8.8l3.5,0.9l-1.1-7.7l4,1.6l1.8,12.7l-6.4-2.1l2,10.2l-2.7,5.5l8.2,1.8 l-3.4,4.8l0.2,6l5,10.6l4.2,4.1l0.2,3.6l3.3,3.8l7.5,3.5l0,0l7.4,4.2l6.2,2l2-0.1l-1.8-5.7l3.4-2.2l1.7-1.5h4.2l-4.8-0.9l-12-0.8 l-3.5-3.6l-1.8-4.6l-3.1,0.4l-2.6-2.2l-3.1-6.6l2.7-2.7l0.1-3.9l-1.8-3.2l0.7-5.3l-1.1-8.2l-1.8-3.7l1.8-1.1l-1.3-2.3l-2.8-1.3 l0.8-2.6l-3.1-2.3l-3.6-7.1l1.6-1.2l-3.3-7.6l-0.7-6.4l-0.3-5.7l2.5-2.4l-3.3-6.3l-1.5-5.9l2.9-4.3l-1.4-5.4l1.6-6.2l-1.3-5.9 l-1.6-1.2l-4.9-10.9l2.1-6.5l-1.7-6.2l0.9-5.8l2.6-5.9l3.2-4l-2-2.5l0.9-2l-1.6-10.6l5.6-3.2l1.1-6.6l-0.9-1.6l-3.8,0.9L601.1,708.9 L601.1,708.9z",
  "colombia": "M578.3,497.2l1.2-2.1l-1.3-1.7l-2-0.4l-2.9,3.1l-2.3,1.4l-4.6,3.2l-4.3-0.5l-0.5,1.3l-3.6,0.1l-3.3,3l-1.4,5.4 l-0.1,2.1l-2.4,0.7l-4.4,4.4l-2.9-0.2l-0.7,0.9l1.1,3.8l-1.1,1.9l-1.8-0.5l-0.9,3.1l2.2,3.4l0.6,5.4l-1.2,1.6l1.1,5.9l-1.2,3.7 l2,1.5l-2.2,3.3l-2.5,4l-2.8,0.4l-1.4,2.3l0.2,3.2l-2.1,0.5l0.8,2l5.6,3.6l1-0.1l1.4,2.7l4.7,0.9l1.6-1l2.8,2.1l2.4,1.5l1.5-0.6 l3.7,3l1.8,3l2.7,1.7l3.4,6.7l4.2,0.8l3-1.7l2.1,1.1l3.3-0.6l4.4,3l-3.5,6.5l1.7,0.1l2.9,3.4l2.2-17.4l0.1-2.8l-0.9-3.6l-2.5-2.4 v-4.6l3.2-1l1.1,0.6l0.2-2.4l-3.3-0.7v-3.9l10.9,0.1l1.9-2.2l1.6,2l1,3.8l1.1-0.8l-1.7-6.4l-1.4-2.2l-2-1.4l2.9-3.1l-0.2-1.5 l-1.5-1.9l-1-4.2l0.5-4.6l1.3-2.1l1.2-3.4l-2-1.1l-3.2,0.7l-4-0.3l-2.3,0.7l-3.8-5.5l-3.2-0.8l-7.2,0.6l-1.3-2.2l-1.3-0.6l-0.2-1.3 l0.8-2.4l-0.4-2.5l-1.1-1.4l-0.6-2.9l-2.9-0.5l1.8-3.7l0.9-4.5l1.8-2.4l2.2-1.8l1.6-3.2L578.3,497.2L578.3,497.2z",
  "ecuador": "M553.1,573.1l-2.4-1.5l-2.8-2.1l-1.6,1l-4.7-0.9l-1.4-2.7l-1,0.1l-5.6-3.6l-3.9,2.5l-3.1,1.4l0.4,2.6l-2.2,4.1 l-1,3.9l-1.9,1l1,5.8l-1.1,1.8l3.4,2.7l2.1-2.9l1.3,2.8l-2.9,4.7l0.7,2.7l-1.5,1.5l0.2,2.3l2.3-0.5l2.3,0.7l2.5,3.2l3.1-2.6l0.9-4.3 l3.3-5.5l6.7-2.5l6-6.7l1.7-4.1L553.1,573.1z",
  "peru": "M584.3,599.5l-2.9-3.4l-1.7-0.1l3.5-6.5l-4.4-3l-3.3,0.6l-2.1-1.1l-3,1.7l-4.2-0.8l-3.4-6.7l-2.7-1.7l-1.8-3l-3.7-3 l-1.5,0.6l0.8,4.9l-1.7,4.1l-6,6.7l-6.7,2.5l-3.3,5.5l-0.9,4.3l-3.1,2.6l-2.5-3.2l-2.3-0.7l-2.3,0.5l-0.2-2.3l1.5-1.5l-0.7-2.7 l-4.4,4l-1.6,4.5l3,6.1l-1.7,2.8l4.1,2.6l4.5,4.1l2,4.7l2.4,2.9l6,12.7l6.2,11.7l5.4,8.4l-0.8,1.8l2.8,5.3l4.6,3.9l10.7,6.9 l11.6,6.4l0.7,2.6l5.9,3.7l2.7-1.6l1.2-3.3l2.8-6.9l-2.8-5.3l1.1-2.1l-1.2-2.4l1.9-3.2l-0.3-5.4l-0.1-4.5l1.1-2.1l-5.5-10.3l-3,1.1 l-2.6-0.7l-0.2-9.7l-4.4,3.8l-4.9-0.2l-2.3-3.4l-3.7-0.3l1-2.8l-3.3-3.8L562,620l1.5-1.1l-0.1-2.7l3.3-1.9l-0.7-3.4l1.3-2.2l0.4-3 l6.2-4.3l4.6-1.2l0.7-1L584.3,599.5L584.3,599.5z",
  "australia": "M1726.7,832l-3-0.5l-1.9,2.9l-0.6,5.4l-2.1,4l-0.5,5.3l3,0.2l0.8,0.3l6.6-4.3l0.6,1.7l4-4.9l3.2-2.2l4.5-7.3 l-2.8-0.5l-4.8,1.2l-3.4,0.9L1726.7,832L1726.7,832z M1776.8,659.7l0.5-2.3l0.1-3.6l-1.6-3.2l0.1-2.7l-1.3-0.8l0.1-3.9l-1.2-3.2 l-2.3,2.4l-0.4,1.8l-1.5,3.5l-1.8,3.4l0.6,2.1l-1.2,1.3l-1.5,4.8l0.1,3.7l-0.7,1.8l0.3,3.1l-2.6,5l-1.3,3.5l-1.7,2.9l-1.7,3.4 l-4.1,2.1l-4.9-2.1l-0.5-2l-2.5-1.6h-1.6l-3.3-3.8l-2.5-2.2l-3.9-2l-3.9-3.5l-0.1-1.8l2.5-3.1l2.1-3.2l-0.3-2.6l1.9-0.2l2.5-2.5 l2-3.4l-2.2-3.2l-1.5,1.2l-2-0.5l-3.5,1.8l-3.2-2l-1.7,0.7l-4.5-1.6l-2.7-2.7l-3.5-1.5l-3.1,0.9l3.9,2.1l-0.3,3.2l-4.8,1.2l-2.8-0.7 l-3.6,2.2l-2.9,3.7l0.6,1.5l-2.7,1.7l-3.4,5.1l0.6,3.5l-3.4-0.6h-3.5l-2.5-3.8l-3.7-2.9l-2.8,0.8l-2.6,0.9l-0.3,1.6l-2.4-0.7 l-0.3,1.8l-3,1.1l-1.7,2.5l-3.5,3.1l-1.4,4.8l-2.3-1.3l-2.2,3.1l1.5,3l-2.6,1.2l-1.4-5.5l-4.8,5.4l-0.8,3.5l-0.7,2.5l-3.8,3.3 l-2,3.4l-3.5,2.8l-6.1,1.9l-3.1-0.2l-1.5,0.6l-1.1,1.4l-3.5,0.7l-4.7,2.4l-1.4-0.8l-2.6,0.5l-4.6,2.3l-3.2,2.7l-4.8,2.1l-3.1,4.4 l0.4-4.8l-3.1,4.6l-0.1,3.7l-1.3,3.2l-1.5,1.5l-1.3,3.7l0.9,1.9l0.1,2l1.6,5l-0.7,3.3l-1-2.5l-2.3-1.8l0.4,5.9l-1.7-2.8l0.1,2.8 l1.8,5l-0.6,5l1.7,2.5l-0.4,1.9l0.9,4.1l-1.3,3.6l-0.3,3.6l0.7,6.5l-0.7,3.7l-2.2,4.4l-0.6,2.3l-1.5,1.5l-2.9,0.8l-1.5,3.7l2.4,1.2 l4,4.1h3.6l3.8,0.3l3.3-2.1l3.4-1.8l1.4,0.3l4.5-3.4l3.8-0.3l4.1-0.7l4.2,1.2l3.6-0.6l4.6-0.2l3-2.6l2.3-3.3l5.2-1.5l6.9-3.2l5,0.4 l6.9-2.1l7.8-2.3l9.8-0.6l4,3.1l3.7,0.2l5.3,3.8l-1.6,1.5l1.8,2.4l1.3,4.6l-1.6,3.4l2.9,2.6l4.3-5.1l4.3-2.1l6.7-5.5l-1.6,4.7 l-3.4,3.2l-2.5,3.7l-4.4,3.5l5.2-1.2l4.7-4.4l-0.9,4.8l-3.2,3.1l4.7,0.8l1.3,2.6l-0.4,3.3l-1.5,4.9l1.4,4l4,1.9l2.8,0.4l2.4,1 l3.5,1.8l7.2-4.7l3.5-1.2l-2.7,3.4l2.6,1.1l2.7,2.8l4.7-2.7l3.8-2.5l6.3-2.7l6-0.2l4.2-2.3l0.9-2l3-4.5l3.9-4.8l3.6-3.2l4.4-5.6 l3.3-3.1l4.4-5l5.4-3.1l5-5.8l3.1-4.5l1.4-3.6l3.8-5.7l2.1-2.9l2.5-5.7l-0.7-5.4l1.7-3.9l1.1-3.7v-5.1l-2.8-5.1l-1.9-2.5l-2.9-3.9 l0.7-6.7l-1.5,1l-1.6-2.8l-2.5,1.4l-0.6-6.9l-2.2-4l1-1.5l-3.1-2.8l-3.2-3l-5.3-3.3l-0.9-4.3l1.3-3.3l-0.4-5.5l-1.3-0.7l-0.2-3.2 l-0.2-5.5l1.1-2.8l-2.3-2.5l-1.4-2.7l-3.9,2.4L1776.8,659.7L1776.8,659.7z",
  "fiji": "M1976.7,674.4l-3.7,2l-1.9,0.3l-3.1,1.3l0.2,2.4l3.9-1.3l3.9-1.6L1976.7,674.4L1976.7,674.4z M1965.7,682.5l-1.6,1 l-2.3-0.8l-2.7,2.2l-0.2,2.8l2.9,0.8l3.6-0.9l1.8-3.3L1965.7,682.5L1965.7,682.5z",
  "new-zealand": "M1868.6,832.8l0.9-2.6l-5.8,2.9l-3.4,3.4l-3.2,1.6l-5.9,4.6l-5.6,3.2l-7,3.2l-5.5,2.4l-4.3,1.1l-11.3,6.1l-6.4,4.6 l-1.1,2.3l5.1,0.4l1.5,2.1l4.5,0.1l4-1.8l6.3-2.8l8.1-6.2l4.7-4.1l6.2-2.3l4-0.1l0.6-2.9l4.6-2.5l7-4.5l4.2-2.9l2.1-2.6l0.5-2.6 l-5.6,2.5L1868.6,832.8L1868.6,832.8z M1897.4,802.3l1.9-5.7l-3.1-1.7l-0.8-3.6l-2.3,0.5l-0.4,4.6l0.8,5.7l0.9,2.7l-0.9,1.1 l-0.6,4.4l-2.4,4.1l-4.2,5l-5.3,2.2l-1.7,2.4l3.7,2.5l-0.8,3.5l-6.9,5.1l1.4,0.9l-0.4,1.6l5.9-2.5l5.9-4.2l4.5-3.4l1.6-1.2l1.5-2.7 l2.8-2l3.8,0.2l4.2-3.8l5.1-5.7l-2.1-0.8l-4.6,2.5l-3.2-0.5l-2.9-2.1l2.3-4.9l-1.2-1.8l-2.9,4.4L1897.4,802.3L1897.4,802.3z",
  "vanuatu": "M1926.6,587.6L1925.8,586.1L1925.7,581.8L1928.4,583.6L1929.3,588.0L1927.8,587.3L1926.6,587.6ZM1569.9,432.7L1568.6,426.0L1572.2,421.4L1579.3,420.3L1584.6,421.1Z"
};

const WORLD_MAP_BG_PATHS = {
  "IR": "M1213.5,324.4l-3.2-2.9l-1.2-2.4l-3.3,1.8l2.9,7.3l-0.7,2l3.7,5.2l0,0l4.7,7.8l3.7,1.9l1,3.8l-2.3,2.2l-0.5,5 l4.6,6.1l7,3.4l3.5,4.9l-0.2,4.6h1.7l0.5,3.3l3.4,3.4l1.7-2.5l3.7,2.1l2.8-1l5.1,8.4l4.3,6.1l5.5,1.8l6.1,4.9l6.9,2.1l5.1-3.1l4-1.1 l2.8,1.1l3.2,7.8l6.3,0.8l6.1,1.5l10.5,1.9l1.2-7.4l7.4-3.3l-0.9-2.9l-2.7-1l-1-5.7l-5.6-2.7l-2.8-3.9l-3.2-3.3l3.9-5.8l-1.1-4 l-4.3-1.1l-1.1-4l-2.7-5.1l1.6-3.5l-2.5-0.9l0.5-4.7l0.5-8l-1.6-5.5l-3.9-0.2l-7.3-5.7l-4.3-0.7l-6.5-3.3l-3.8-0.6l-2.1,1.2 l-3.5-0.2l-3,3.7l-4.4,1.2l-0.2,1.6l-7.9,1.7l-7.6-1.1l-4.3-3.3l-5.2-1.3l-2.5-4.8l-1.3,0.3l-3.8-3.4l1.2-3.1l-1.9-1.9l-1.9,0.5 l-5.3,4.7l-1.8,0.2L1213.5,324.4L1213.5,324.4z",
  "IQ": "M1207.3,334.9l-6.2-0.9l-2.1,1l-2.1,4.1l-2.7,1.6l1.2,4.7l-0.9,7.8l-11,6.7l3.1,7.7l6.7,1.7l8.5,4.5l16.7,12.7 l10.2,0.5l3.2-6.1l3.7,0.5l3.2,0.4l-3.4-3.4l-0.5-3.3h-1.7l0.2-4.6l-3.5-4.9l-7-3.4l-4.6-6.1l0.5-5l2.3-2.2l-1-3.8l-3.7-1.9 l-4.7-7.8l0,0l-2.3,1.1L1207.3,334.9L1207.3,334.9z",
  "JO": "M1186.6,367.6l-3.1-7.7l-9.6,6.7l-6.3-2.5l-0.7,2l0.4,3.9l-0.6,1.9l0.4,2.4l-1.7,10.2l0.3,0.9l6.1,1l2.1-2l1.1-2.3 l4-0.8l0.7-2.2l1.7-1l-6.1-6.4l10.4-3.1L1186.6,367.6L1186.6,367.6z",
  "KZ": "M1308.8,223.8l-9-1.3l-3.1,2.5l-10.8,2.2l-1.7,1.5l-16.8,2.1l-1.4,2.1l5,4.1l-3.9,1.6l1.5,1.7l-3.6,2.9l9.4,4.2 l-0.2,3l-6.9-0.3l-0.8,1.8l-7.3-3.2l-7.6,0.2l-4.3,2.5l-6.6-2.4l-11.9-4.3l-7.5,0.2l-8.1,6.6l0.7,4.6l-6-3.6l-2.1,6.8l1.7,1.2 l-1.7,4.7l5.3,4.3l3.6-0.2l4.2,4.1l0.2,3.2l2.8,1l4.4-1.3l5-2.7l4.7,1.5l4.9-0.3l1.9,3.9l0.6,6l-4.6-0.9l-4,1l0.9,4.5l-5-0.6l0.6,2 l3.2,1.6l3.7,5.5l6.4,2.1l1.5,2.1l-0.7,2.6l0.7,1.5l1.8-2l5.5-1.3l3.8,1.7l4.9,4.9l2.5-0.3l-6.2-22.8l11.9-3.6l1.1,0.5l9.1,4.5 l4.8,2.3l6.5,5.5l5.7-0.9l8.6-0.5l7.5,4.5l1.5,6.2l2.5,0.1l2.6,5l6.6,0.2l2.3,3h1.9l0.9-4.5l5.4-4.3l2.5-1.2l0.3-2.7l3.1-0.8 l9.1,2.1l-0.5-3.6l2.5-1.3l8.1,2.6l1.6-0.7l8.6,0.2l7.8,0.6l3.3,2.2l3.5,0.9l-1.7-3.5l2.9-1.6l-8.7-10.7l9-2.4l2-1.4l-1-11.1l10.7,2 l1.6-2.8l-2.5-6.2l3.8-0.6l1.8-4.2l-4.3-3.8l-6,0.9l-3.3-2.6l-3.9-1.2l-4.1-3.6l-3.2-1.1l-6.2,1.6l-8.3-3.6l-1.1,3.3l-18.1-15.5 l-8.3-4.7l0.8-1.9l-9.1,5.7l-4.4,0.4l-1.2-3.3l-7-2.1l-4.3,1.5L1308.8,223.8L1308.8,223.8z",
  "KG": "M1387.2,302.6l-3.5-0.9l-3.3-2.2l-7.8-0.6l-8.6-0.2l-1.6,0.7l-8.1-2.6l-2.5,1.3l0.5,3.6l-9.1-2.1l-3.1,0.8l-0.3,2.7 l1.8,0.6l-3.1,4.1l4.6,2.3l3.2-1.6l7.1,3.3l-5.2,4.5l-4.1-0.6l-1.4,2l-5.9-1.1l0.6,3.7l5.4-0.5l7.1,2l9.5-0.9l1-1.5l-1.1-1.5l4-3 l3.2-1.2l5.7,0.9l0.6-4l6.4-0.8l1-2.4l6.8-3.4L1387.2,302.6L1387.2,302.6z",
  "LB": "M1167.8,360.5l0.9-3.5l2.6-2.4l-1.2-2.5l-2.4-0.3l-0.1,0.2l-2.1,4.5l-1.3,5.2h1.8l0.4-1.1L1167.8,360.5 L1167.8,360.5z",
  "LK": "M1432.2,532.7l2.3-1.8l0.6-6.6l-3-6.6l-2.9-4.5l-4.1-3.5l-1.9,10.3l1.4,9.1l2.8,5.1L1432.2,532.7L1432.2,532.7z",
  "LR": "M929.4,523.3l-1.6-0.2l-1.1,2.6l-1.6-0.1l-1.1-1.3l0.4-2.6l-2.3-3.9l-1.5,0.7l-1.2,0.2l-2.6,3l-2.6,3.4l-0.3,1.9 l-1.3,2l3.7,4.1l4.8,3.5l5.1,4.8l5.7,3.1l1.5-0.1l0.5-5.2l0.5-0.8l-0.2-2.5l-2.3-2.7l-1.8-0.4l-1.6-1.8l1.2-2.8l-0.6-3.1 L929.4,523.3L929.4,523.3z",
  "LS": "M1128.1,766.5l1.1-2l3.1-1l1.1-2.1l1.9-3.1l-1.7-1.9l-2.3-2l-2.6,1.3l-3.1,2.5l-3.2,4l3.7,4.9L1128.1,766.5 L1128.1,766.5z",
  "LT": "M1100.4,221.2l-5-2.9l-2.5-0.4l-0.9-1.3l-4.4,0.6l-7.9-0.4l-5,1.9l1.7,5l5,1.1l2.2,0.9l-0.2,1.7l0.6,1.5l2.5,0.6 l1.4,1.9h4.6l4.8-2.2l0.5-3.4l3.5-2L1100.4,221.2L1100.4,221.2z",
  "LV": "M1102.1,210.1h-3.8l-4.4-2.2l-2.1-0.7l-3.7,1l-0.2,4.6l-3.6,0.1l-4.4-4.5l-4,2.1l-1.7,3.7l0.5,4.5l5-1.9l7.9,0.4 l4.4-0.6l0.9,1.3l2.5,0.4l5,2.9l2.6-1l4.6-2.3l-2.1-3.6l-1-2.8L1102.1,210.1L1102.1,210.1z",
  "LY": "M1111.8,371.4l-1.5-2.1l-5.4-0.8l-1.8-1.1h-2l-2-2.8l-7.3-1.3l-3.6,0.8l-3.7,3l-1.5,3.1l1.5,4.8l-2.4,3l-2.5,1.6 l-5.9-3.1l-7.7-2.7l-4.9-1.2l-2.8-5.7l-7.2-2.8l-4.5-1.1l-2.2,0.6l-6.4-2.2l-0.1,4.9l-2.6,1.8l-1.5,2l-3.7,2.5l0.7,2.6l-0.4,2.7 l-2.6,1.4l1.9,5.6l0.4,3l-0.9,5.2l0.5,2.9l-0.6,3.5l0.5,4l-2.1,2.6l3.4,4.7l0.2,2.7l2,3.6l2.6-1.2l4.3,2.9l2.5,4l8.8,2.8l3.1,3.5 l3.9-2.4l5.4-3.5l22.3,12.2l22.4,12.2v-2.7h6.3l-0.5-12.7l-1-23.4l-1.3-22.7l-2-5.1l1.2-3.9l-1.1-2.7L1111.8,371.4L1111.8,371.4z",
  "MG": "M1255.7,658.4l-1.1-4.2l-1.4-2.7l-1.8-2.7l-2,2.8l-0.3,3.8l-3.3,4.5l-2.3-0.8l0.6,2.7l-1.8,3.2l-4.8,3.9l-3.4,3.7 h-2.4l-2.2,1.2l-3.1,1.3l-2.8,0.2l-1,4.1l-2.2,3.5l0.1,5.9l0.8,4l1.1,3l-0.8,4.1l-2.9,4.8l-0.2,2.1l-2.6,1.1l-1.3,4.6l0.2,4.6l1.6,5 l-0.1,5.7l1.2,3.3l4.2,2.3l3,1.7l5-2.7l4.6-1.5l3.1-7.4l2.8-8.9l4.3-12l3.3-8.8l2.7-7.4l0.8-5.4l1.6-1.5l0.7-2.7l-0.8-4.7l1.2-1.9 l1.6,3.8l1.1-1.9l0.8-3.1l-1.3-2.9L1255.7,658.4L1255.7,658.4z",
  "MW": "M1169.2,661.5l0.1-2.3l-1.2-1.9l0.1-2.8l-1.5-4.7l1.7-3.5l-0.1-7.7l-1.9-4.1l0.2-0.7l0,0l-1.1-1.7l-5.4-1.2l2.6,2.8 l1.2,5.4l-1,1.8l-1.2,5.1l0.9,5.3l-1.8,2.2l-1.9,5.9l2.9,1.7l3,3l1.6-0.6l2.1,1.6l0.3,2.6l-1.3,2.9l0.2,4.5l3.4,4l1.9-4.5l2.5-1.3 l-0.1-8.2l-2.2-4.6l-1.9-2h-0.3v0.8l1.1,0.3l1,3.4l-0.2,0.8l-1.9-2.5l-1,1.6L1169.2,661.5L1169.2,661.5z",
  "ML": "M1000.3,450.3l-6.1,0.6l-0.1-4l-2.6-1.1l-3.4-1.8l-1.3-3l-18.6-13.8l-18.4-13.9l-8.4,0.1l2.4,27.4l2.4,27.5l1,0.8 l-1.3,4.4l-22.3,0.1l-0.9,1.4l-2.1-0.4l-3.2,1.3l-3.8-1.8l-1.8,0.2l-1,3.7l-1.9,1.2l0.2,3.9l1.1,3.7l2.1,1.8l0.4,2.4l-0.3,2l0.3,2.3 h0.9l1.5-0.8l0.9,0.2l1.5,1.6l2.4,0.5l1.6-1.4l1.8-0.8l1.3-0.9l1.1,0.2l1.3,1.4l0.6,1.7l2.3,2.7l-1.2,1.6l-0.2,2.1l1.2-0.6l0.7,0.7 l-0.3,1.9l1.7,1.8l0.7-0.6l1.6,1l4.3,0.1l1-1.9l1,0.1l1.6-0.7l0.9,2.7l1.3-0.8l2.3-0.9l-0.4-3.7l1.6-2.7l-0.2-2.2l4.5-5.2l0.8-4.4 l1.6-1.6l2.7,0.9l2.3-1.3l0.8-1.6l4.3-2.9l1.1-2l5.2-2.6l3-0.9l1.4,1.2h3.6l3.6-0.3l2-2.2l7.6-0.6l4.9-1l0.5-3.9l3-4.3L1000.3,450.3 L1000.3,450.3z",
  "MR": "M949.8,413.3l-20.3-15.5l-0.2,9.7l-17.9-0.3l-0.2,16.3L906,424l-1.4,3.3l0.9,9.2l-21.6-0.1l-1.2,2.2l2.8,2.7l1.4,3 l-0.7,3.2l0.6,3.2l0.5,6.3l-0.8,5.9l-1.7,3.2l0.4,3.4l2-2l2.7,0.5l2.8-1.4h3.1l2.6,1.8l3.7,1.7l3.2,4.7l3.6,4.4l1.9-1.2l1-3.7 l1.8-0.2l3.8,1.8l3.2-1.3l2.1,0.4l0.9-1.4l22.3-0.1l1.3-4.4l-1-0.8l-2.4-27.5l-2.4-27.4L949.8,413.3L949.8,413.3z",
  "MT": "M1053.6,344l-0.2-0.2l-0.5-0.5l-0.5-0.1l0.1,0.6l0.4,0.4h0.5L1053.6,344L1053.6,344z M1052.2,342.8L1052.2,342.8 v-0.2l-0.3-0.1l-0.4,0.1l0.1,0.1l0.3,0.2L1052.2,342.8z",
  "NE": "M1051.3,425.6l-8.8-2.8l-18.6,12.2l-15.8,12.5l-7.8,2.8l0.1,14.6l-3,4.3l-0.5,3.9l-4.9,1l-7.6,0.6l-2,2.2l-3.6,0.3 l-0.5,3.1l0.8,2.9l3.1,4.1l0.2,3.1l6.4,1.4l-0.1,4.4l1.9-1.9h2l4.3,3.7l0.3-5.7l1.6-2.6l0.8-3.6l1.4-1.4l6-0.8l5.6,2.4l2.1,2.4 l2.9,0.1l2.6-1.5l6.8,3.3l2.8-0.2l3.3-2.7l3.3,0.2l1.6-0.9l3,0.4l4.3,1.8l4.3-3.5l1.3,0.2l3.9,7l1-0.2l0.2-2l1.6-0.4l0.5-2.9 l-3.6-0.2v-4.1l-2.4-2.3l2.3-8.4l6.9-6l0.2-8.3l1.8-12.9l1.1-2.7l-2.3-2.2l-0.2-2.1l-2-1.6l-1.6-9.9l-3.9,2.4L1051.3,425.6 L1051.3,425.6z",
  "NG": "M1055.8,492.7l-1,0.2l-3.9-7l-1.3-0.2l-4.3,3.5l-4.3-1.8l-3-0.4l-1.6,0.9l-3.3-0.2l-3.3,2.7l-2.8,0.2l-6.8-3.3 l-2.6,1.5l-2.9-0.1l-2.1-2.4l-5.6-2.4l-6,0.8l-1.4,1.4l-0.8,3.6l-1.6,2.6l-0.3,5.7l-0.2,2.1l1.2,3.8l-1.1,2.5l0.6,1.7l-2.7,4 L993,514l-1,4l0.1,4.1l-0.3,10.2h4.9h4.3l3.9,4.2l1.9,4.6l3,3.9l4.5,0.2l2.2-1.4l2.1,0.3l5.8-2.3l1.4-4.5l2.7-6.1l1.6-0.1l3.3-3.7 l2.1-0.1l3.2,2.6l3.9-2.2l0.5-2.6l1.2-2.6l0.8-3.2l3-2.6l1.1-4.5l1.2-1.4l0.7-3.3l1.5-4l4.6-5l0.3-2.1l0.6-1.1L1055.8,492.7 L1055.8,492.7z",
  "NI": "M514.1,476.8l-1.9-0.2l-0.9,0.9l-2,0.8h-1.4l-1.3,0.8l-1.1-0.3l-0.9-0.9l-0.6,0.2l-0.8,1.5l-0.5-0.1l-0.3,1.3 l-2.1,1.8l-1.1,0.7l-0.6,0.8l-1.5-1.3l-1.4,1.7h-1.2l-1.3,0.2l-0.2,3.1h-0.8l-0.8,1.5l-1.8,0.3l-0.4,0.4l-0.9-1l-0.7,1l2.6,2.9 l2.2,2l1,2.1l2.5,2.6l1.8,2l0.9-0.8l3.5,1.7l1.4-0.8l1.7,0.5l0.8,1.3l1.7,0.4l1.4-1.3l-0.8-1.1l-0.1-1.7l1.2-1.6l-0.2-1.7l0.7-2.7 l0.9-0.7l0.1-2.8l-0.2-1.7l0.4-2.8l0.9-2.5l1.4-2.2l-0.3-2.3l0.4-1.4L514.1,476.8L514.1,476.8z",
  "NP": "M1455.2,394.8l-6.5-0.6l-6.4-1.5l-5-2.8l-4.5-1.2l-2.5-3.1l-3.2-0.9l-6.4-4.1l-4.7-2l-1.9,1.5l-2.8,2.9l-0.9,5.9 l5.7,2.5l5.8,3.1l7.7,3.5l7.6,0.9l3.8,3.2l4.3,0.6l6.8,1.5l4.6-0.1l0.1-2.5l-1.5-4.1L1455.2,394.8L1455.2,394.8z",
  "PG": "M1850.7,615.6l0.9-1.8l-2.4-2.2l-2.5-4l-1.6-1.5l-0.5-1.9l-0.8,0.7l0.9,4.8l2.2,4l2.2,2.5L1850.7,615.6 L1850.7,615.6z M1829.5,607l2.1-3.9l0.4-3.5l-1.1-1l-3.4,0.1l0.4,3.7l-3.3,2.3l-1.7,2.2l-3.2,0.5l-0.4-3.4l-0.8,0.1l-1,3.1l-3.1,0.5 l-5-0.9l-0.6,1.9l3.1,1.8l4.5,1.9h2.9l3-1.5l3.2-1.6l1-1.8L1829.5,607L1829.5,607z M1801.7,619.2l-0.9-4.3l5.2-0.7l-1.1-3.3l-9.1-4 l-0.6-3.7l-2.9-3.2l-3.7-3.3l-10.2-3.6l-9.6-4.4l-1,20.7l-1.5,20.8l5.7,0.2l3.1,1.1l4.6-2.2l-0.3-4.7l3.6-2.1l4.9-1.8l7,2.8l2.4,5.6 l2.9,3.5l3.9,4l5.5,1l4.8,0.7l1.1,1.6l3.8-0.4l0.8-1.8l-5.6-2.7l1.8-1.2l-4.2-1.1l0.5-2.8l-3.2,0.2l-3-6.8L1801.7,619.2 L1801.7,619.2z M1836.4,600.8l-0.5-3.3l-2-2.1l-2.1-2.6l-2.3-1.5l-1.9-1.4l-2.9-1.8l-1.6,1.5l3.9,1.9l3.1,2.7l2.4,2.1l1.2,2.4 l0.8,3.8L1836.4,600.8L1836.4,600.8z",
  "PH": "M1684.6,518.6l-0.6-2.3l-0.8-3.2l-4.8-3l0.8,4.9l-3.9,0.2l-0.7,2.8l-4.2,1.7l-2.2-2.8l-2.8,2.4l-3.4,1.7l-1.9,5.4 l1.1,1.9l3.9-3.6l2.7,0.3l1.5-2.7l3.8,3l-1.5,3.1l1.9,4.6l6.8,3.7l1.4-3l-2.1-4.7l2.4-3.2l2.5,6.4l1.5-5.8l-0.6-3.5L1684.6,518.6 L1684.6,518.6z M1670.1,506.8v-6.1l-3.6,6.1l0.5-4.2l-3,0.3l-0.3,4l-1.2,1.8l-1,1.7l3.8,4.4l1.6-1.9l1.4-4L1670.1,506.8 L1670.1,506.8z M1640,512.9l2.6-4.4l3.4-3.5l-1.5-5.2l-2.4,6.3l-2.9,4.4l-3.8,4l-2.4,4.4L1640,512.9L1640,512.9z M1657.4,496.5 l1.2,3l-0.1,3.3l0.5,2.9l3.3-1.9l2.4-2.7l-0.2-2.6h-3.6L1657.4,496.5L1657.4,496.5z M1677.4,494.8l-1.8-2.4l-5.4-0.1l4,4.8l0.3,2.4 l-3.3-0.5l1.2,3.9l1.7,0.3l0.7,4.5l2.5-1.4l-1.7-4l-0.4-2.1l4.5,1.7L1677.4,494.8L1677.4,494.8z M1654.5,489l-2.2-2.3l-4.8-0.2 l3.4,4.8l2.8,3.2L1654.5,489L1654.5,489z M1648.1,454.4h-3.3l-0.9,5.8l1.1,9.9l-2.6-2l1.2,6l1.2,2.8l3.3,3.7l0.4-2.3l1.8,1.4 l-1.5,1.7l0.1,2.6l2.9,1.4l5-0.9l4,3.8l1.1-2.4l2.5,3.4l4.8,3.1l0.2-2.9l-2-1.6l0.1-3.4l-7.5-3.6l-2.3,0.8l-3.1-0.7l-2-5.1l0.1-5.1 l3-2.1l0.6-5.3l-2.7-4.6l0.4-2.6l-0.7-1.6l-1.5,1.6L1648.1,454.4L1648.1,454.4z",
  "PS": "M1166.9,366.1l-2-0.9l-0.7,4.3l1.4,0.7l-1.2,0.8l-0.1,1.7l2.4-0.8l0.6-1.9L1166.9,366.1L1166.9,366.1z",
  "RO": "M1108.1,266.3h-2.1l-1,1.5l-3.6,0.6l-1.6,0.9l-2.4-1.5h-3.2l-3.2-0.7l-1.9,1.3l-2.9,1.3l-1.9,4.2l-2.6,4.3l-3.8,1.1 l2.9,2.5l0.8,1.9l3.2,1.5l0.7,2.5l3.1,1.8l1.4-1.3l1.4,0.7l-1.1,1.1l1,1l1.8,2.6l1.9-0.5l4,1l7.5,0.3l2.3-1.6l5.8-1.4l4,2.2l3,0.7 l0.4-7.4l1.6,0.5l2.3-1.3l-0.4-1.6l-2.4-1.1l-2.2,1l-2.4-1.1l-1.3-2.8l0.2-2.7l-0.6-2.7l-3.4-3.7l-1.9-2.6l-1.8-1.9L1108.1,266.3 L1108.1,266.3z",
  "RW": "M1147.6,579.4l-3.3,1.9l-1.4-0.6l-1.6,1.8l-0.2,3.8l-0.8,0.4l-0.6,3.5l3.5,0.5l1.7-3.6l3,0.4l0,0l1.6-0.8l0.4-3.7 L1147.6,579.4L1147.6,579.4z",
  "SA": "M1228.7,387l-10.2-0.5l-16.7-12.7l-8.5-4.5l-6.7-1.7l-0.9,1l-10.4,3.1l6.1,6.4l-1.7,1l-0.7,2.2l-4,0.8l-1.1,2.3 l-2.1,2l-6.1-1l-0.5,2.5v2.2l-0.6,3.5h2.7l3.2,4.4l3.7,5.1l2.5,4.7l1.7,1.5l1.7,3.3l-0.2,1.4l2.1,3.7l3,1.3l2.8,2.5l3.6,7v3.8 l0.9,4.4l4,6.1l2.5,1l4.1,4.4l1.9,5.2l3.2,5.3l3,2.3l0.6,2.5l1.8,1.9l0.9,2.8l2.3-2.1l-0.7-2.7l1.2-3.1l2.4,1.7l1.5-0.6l6.4-0.2 l1,0.7l5.4,0.6l2.1-0.3l1.6,2.1l2.5-1l3.5-6.7l5-2.9l15.7-2.4l16.1-6.4l2.6-12.7l-2.9-4.5l-1,1.3l-16.8-3.2l-2.6-6.4l-0.4-1.5 l-1.2-2.4l-1.5,0.4l-1.8-1.2l-1-1.6l-0.9-2.1l-1.7-1.8l-1-2.1l0.4-2.1l-0.6-2.7l-4-2.6l-1.2-2.3l-2.9-1.4l-2.7-5.5l-3.8,0.2 l-1.7-3.1L1228.7,387L1228.7,387z",
  "SD": "M1180.8,468.5l0.4-4.2l1.6-2l4-1l2.6-3.6l-3.1-2.4l-2.2-1.6l-2.5-7.6l-1.1-6.5l1.1-1.2l-2.1-6.2h-21.8h-21.4h-22.1 l0.5,12.7h-6.3v2.7l1.1,25.2l-4.8-0.4l-2.4,4.7l-1.4,3.9l1.2,1.5l-1.8,1.9l0.7,2.7l-1.4,2.6l-0.5,2.4l2-0.4l1.2,2.5l0.1,3.7l2.1,1.8 v1.6l0.7,2.7l3.3,4v2.6l-0.8,2.6l0.3,2l2,1.8l0.5,0.3l1.7-0.7l1.9-1.2l1.3-5.7l1.5-2.9l4-0.9l1,1.8l3,3.7l1.5,0.5l2-1.1l4.1,0.3 l0.8,1.3h5.5l0.2-1.3l2.9-1.2l0.5-1.9l2.1-1.3l4.8,3.7l2.8-0.7l2.7-4.5l3-3.5l-0.6-3.9l-1.4-1.8l3.4-0.3l0.3-1.5l2.6,0.5l-0.5,4.7 l0.8,4.6l2.9,2.5l0.7,2.2v3.1l0.8,0.1v-0.7l1.4-6.7l2.6-1.8l0.5-2.6l2.3-4.8l3.2-3.2l2.1-6.2l0.7-5.5l-0.7-2.5L1180.8,468.5 L1180.8,468.5z",
  "SI": "M1059.4,277l-1.2-2.1l-0.8-0.1l-0.9,1.1l-4.3,0.1l-2.4,1.4l-4.2-0.4l-0.3,3l1.4,2.7l-1.1,0.5l3.5,0.2l0.8-1l1.8,1 l2,0.1l-0.2-1.7l1.7-0.6l0.3-2.5L1059.4,277L1059.4,277z",
  "SL": "M919.4,518.7l-1.5,0.3v-2.3L917,515l0.2-1.8l-1.2-2.7l-1.5-2.3H910l-1.3,1.2l-1.5,0.2l-1,1.4l-0.7,1.7l-3,2.8 l0.7,4.7l0.9,2.3l2.9,3.5l4.1,2.5l1.5,0.5l1.3-2l0.3-1.9l2.6-3.4L919.4,518.7L919.4,518.7z",
  "SO": "M1223.4,505.7l-2.6-2.7l-1.2-2.6l-1.8-1.2l-2,3.4l-1.1,2.3l2.2,3.5l2.1,3.1l2.2,2.2l18.5,7.6l4.8-0.1l-15.4,19.1 l-7.4,0.3l-4.9,4.5l-3.6,0.1l-1.5,2l-4.8,7.2l0.2,23.2l3.3,5.3l1.3-1.5l1.3-3.4l6.1-7.7l5.3-4.8l8.3-6.4l5.6-5.1l6.4-8.7l4.7-7.1 l4.6-9.3l3.2-8.2l2.5-7.1l1.3-6.8l1.1-2.3l-0.2-3.4l0.4-3.7l-0.2-1.7h-2.1l-2.6,2.2l-2.9,0.6l-2.5,0.9l-1.8,0.2l0,0l-3.2,0.2 l-1.9,1.1l-2.8,0.5l-4.8,1.9l-6.1,0.8l-5.2,1.6L1223.4,505.7L1223.4,505.7z",
  "SR": "M668,533.8l-4.6,0.5l-0.6,1.1l-6.7-1.2l-1,5.7l-3.5,1.6l0.3,1.5l-1.1,3.3l2.4,4.6l1.8,0.1l0.7,3.5l3.3,5.6l3.1,0.5 l0.5-1.3l-0.9-1.3l0.5-1.8l2.3,0.6l2.7-0.7l3.2,1.4l1.4-2.7l0.6-2.9l1-2.8l-2.1-3.7l-0.4-4.4l3.1-5.5L668,533.8L668,533.8z",
  "SS": "M1166,508.7l-0.7-2.2l-2.9-2.5l-0.8-4.6l0.5-4.7l-2.6-0.5l-0.3,1.5l-3.4,0.3l1.4,1.8l0.6,3.9l-3,3.5l-2.7,4.5 l-2.8,0.7l-4.8-3.7l-2.1,1.3l-0.5,1.9l-2.9,1.2l-0.2,1.3h-5.5l-0.8-1.3l-4.1-0.3l-2,1.1l-1.5-0.5l-3-3.7l-1-1.8l-4,0.9l-1.5,2.9 l-1.3,5.7l-1.9,1.2l-1.7,0.7l3.8,2.5l3.1,2.6l0.1,2l3.8,3.4l2.4,2.7l1.5,3.8l4.2,2.5l0.9,2.1l3.5,5.2l2.5,0.8l1.5-1.1l2.6,0.4 l3.1-1.3l1.4,2.7l5,4.2l0,0l2.3-1.7l3.5,1.4l4.5-1.5l4,0.1l3.4-3l3.4-3.8l3.8-4.2l-3.5-6.9l-2.6-1.5l-1-2.5l-2.9-3.1l-3.4-0.5 l1.8-3.6l3-0.1l0.8-2l-0.2-5l-0.8-0.1L1166,508.7L1166,508.7z",
  "ST": "M1014.1,571.4l0.5-0.8v-0.5l-0.3-0.5h-0.4l-0.5,0.4l-0.3,0.4v0.3l0.1,0.7l0.1,0.3l0.3,0.2L1014.1,571.4 L1014.1,571.4z M1018.4,562.2l0.2-0.4v-0.2l-0.1-0.1l-0.1-0.1l-0.2,0.1l-0.3,0.5l0.1,0.2l0.2,0.2L1018.4,562.2L1018.4,562.2z",
  "SZ": "M1150.5,736.6l-2.7-1.2l-1.6,0.5l-0.7,1.8l-1.6,2.4l-0.1,2.2l3,3.5l3.3-0.7l1.3-2.8l-0.3-2.8L1150.5,736.6 L1150.5,736.6z",
  "TG": "M981.7,502.2l-4.9-0.1l-0.4,1.9l2.4,3.3l-0.1,4.6l0.6,5.1l1.4,2.3l-1.2,5.7l0.4,3.2l1.5,4l1.2,2.2l4.6-1.3l-1.4-4.4 l0.2-14.6l-1.1-1.3l-0.2-3.1l-2-2.3l-1.7-1.9L981.7,502.2L981.7,502.2z",
  "TL": "M1676.8,631.9l4.9-1.8l6-2.8l2.2-1.7l-2-0.8l-1.8,0.8l-4,0.2l-4.9,1.4l-0.8,1.5l0.5,1.3L1676.8,631.9L1676.8,631.9z",
  "TM": "M1325.6,334.2l-0.8-4l-7.7-2.7l-6.2-3.2l-4.2-3l-7-4.4l-4.3-6.4l-2-1.2l-5.5,0.3l-2.3-1.3l-1.9-4.9l-7.8-3.3 l-3.3,3.6l-3.8,2.2l1.6,3.1l-5.8,0.1l-2.5,0.3l-4.9-4.9l-3.8-1.7l-5.5,1.3l-1.8,2l2.5,4l-0.5-4.5l3.7-1.6l2.4,3.6l4.6,3.7l-4,2 l-5.3-1.5l0.1,5.2l3.5,0.4l-0.4,4.4l4.5,2.1l0.7,6.8l1.8,4.5l4.4-1.2l3-3.7l3.5,0.2l2.1-1.2l3.8,0.6l6.5,3.3l4.3,0.7l7.3,5.7 l3.9,0.2l1.6,5.5l5.9,2.4l3.9-0.8l0.4-3l4-0.9l2.5-2l-0.1-5.2l4.1-1.2l0.3-2.3l2.9,1.7L1325.6,334.2L1325.6,334.2z",
  "TN": "M1038,361.4l-2-1l-1.5-3l-2.8-0.1l-1.1-3.5l3.4-3.2l0.5-5.6l-1.9-1.6l-0.1-3l2.5-3.2l-0.4-1.3l-4.4,2.4l0.1-3.3 l-3.7-0.7l-5.6,2.6l-1,3.3l1,6.2l-1.1,5.3l-3.2,3.6l0.6,4.8l4.5,3.8v1.5l3.4,2.6l2.6,11.3l2.6-1.4l0.4-2.7l-0.7-2.6l3.7-2.5l1.5-2 l2.6-1.8L1038,361.4L1038,361.4z",
  "TT": "M635.4,507.7l0.1-0.2v-0.6l0.2-0.4l-0.2-0.4l-0.1-0.6l0.1-0.5v-0.7l0.2-0.3l0.5-0.8h-0.9l-0.6,0.2l-1.1,0.1 l-0.5,0.2l-0.7,0.1L632,504l0.1,0.1l0.5,0.2l0.2,0.2l0.1,0.2l0.1,0.4l-0.3,1.7l-0.1,0.1L632,507l-0.2,0.3l-1.4,0.8l0.8-0.1l0.9,0.1 l2.4-0.1L635.4,507.7L635.4,507.7z M637.2,501l1.2-0.5l0.1-0.4h-0.2l-0.8,0.3l-0.6,0.5v0.2L637.2,501z",
  "UG": "M1167.6,545.1l-3.4,3l-4-0.1l-4.5,1.5l-3.5-1.4l-2.3,1.7l0,0l-0.3,7.5l2.3,0.8l-1.8,2.3l-2.2,1.7l-2.1,3.3l-1.2,3 l-0.3,5.1l-1.3,2.4l-0.1,4.8l1.4,0.6l3.3-1.9l2-0.8l6.2,0.1l0,0l-0.3-2.5l2.6-3.7l3.5-0.9l2.4-1.5l2.9,1.2l0.3,0.5v-0.3l1.6-2.6 l2.7-4.2l2.1-4.7l-2.6-7.3l-0.7-3.2L1167.6,545.1L1167.6,545.1z",
  "KP": "M1644.7,302.3L1644.7,302.3l-5.5-3.6l0.1,3.5l-6.3,2.6l2.7,3.3l-4.6-0.2l-3.6-2l-1,4.4l-3.8,3.4l-2.1,4l3.3,1.7 l3.4,0.7l0.8,1l0.4,3.5l1.1,1.2l-0.9,0.7l-0.1,2.9l1.9,1l1.6,0.6l0.8,1.2l1.3-0.5v-1.3l3.1,1.3l0.1-0.6l2.4,0.2l0.7-2.9l3.5-0.3 l2.1-0.4l-0.1-1.6l-4.3-2.8l-2.6-1l0.2-0.7l-1.2-2.8l1.3-1.7l2.9-1l1-1.9l0.3-1.1l1.9-1.4l-2.8-4.5l0.3-2.1l0.9-2l2.2,0.3l0,0l0,0 l0,0L1644.7,302.3L1644.7,302.3z",
  "KR": "M1637.3,331.7l6.2,5.5l-3.4,1.1l5.2,6.8l1.1,4.8l2.1,3.5l4.5-0.5l3.2-2.7l4.2-1.2l0.5-3.6l-3.4-7.5l-3.3-4.2 l-8.2-7.6l0.1,1.6l-2.1,0.4l-3.5,0.3l-0.7,2.9l-2.4-0.2L1637.3,331.7L1637.3,331.7z",
  "UY": "M679.9,668.5L683.5,667.9L689.0,672.2L691.1,672.1L696.8,675.6L701.2,678.7L704.4,682.5L701.9,685.1L703.5,688.3L701.1,691.8L694.8,694.9L690.7,693.8L687.7,694.4L682.6,692.0L678.8,692.2L675.4,689.1L675.8,685.5L677.0,684.2L677.0,678.7L678.5,673.0L679.9,668.5Z",
  "UZ": "M1310.9,270.8L1310.7,250.3L1325.0,247.0L1326.1,247.5L1334.7,251.5L1339.2,253.6L1344.5,258.6L1351.0,257.8L1360.6,257.3L1367.2,261.4L1366.8,267.0L1369.5,267.0L1370.6,271.6L1377.7,271.7L1379.2,274.4L1381.3,274.3L1383.7,270.4L1391.1,266.5L1394.2,265.5L1395.9,266.0L1391.2,269.6L1395.3,271.7L1399.3,270.3L1405.9,273.2L1398.8,277.2L1394.5,276.7L1392.2,276.8L1391.4,275.3L1392.6,272.7L1385.2,274.0L1383.4,277.6L1380.8,280.6L1376.1,280.4L1374.7,282.8L1378.8,284.2L1380.0,288.3L1376.8,293.9L1372.6,292.8L1369.6,292.7L1369.7,289.3L1362.3,286.9L1356.5,284.2L1352.9,281.6L1346.5,277.8L1343.8,272.0L1341.9,271.0L1335.9,271.3L1333.8,270.1L1333.2,265.7L1325.7,262.8L1321.0,266.0L1316.3,267.9L1317.2,270.7L1310.9,270.8Z",
  "VE": "M662.6,471.6L663.3,473.2L661.3,475.3L655.1,477.4L651.1,478.2L649.5,479.5L645.1,478.1L640.9,477.4L639.9,477.9L642.4,479.4L642.2,483.1L642.9,486.6L647.6,487.1L647.9,488.3L644.0,489.8L643.3,492.2L641.0,493.1L636.9,494.4L635.8,496.1L631.5,496.5L628.5,493.5L626.8,488.0L625.3,486.0L623.3,484.8L626.1,482.0L625.9,480.8L624.3,479.1L623.2,475.5L623.6,471.5L624.9,469.6L625.9,466.6L623.9,465.6L620.7,466.3L616.7,466.0L614.5,466.6L610.6,461.8L607.4,461.1L600.2,461.6L598.9,459.7L597.5,459.2L597.3,458.1L598.0,456.0L597.6,453.8L596.3,452.5L595.6,450.0L592.7,449.6L594.3,446.4L595.0,442.4L596.6,440.3L598.7,438.7L600.1,435.9L603.7,435.0L603.5,436.3L600.3,437.0L602.1,439.5L602.0,442.4L599.6,445.6L601.7,450.0L604.1,449.7L605.3,445.7L603.6,443.7L603.3,439.5L610.2,437.2L609.5,434.6L611.4,432.9L613.4,436.8L617.3,436.9L620.9,440.0L621.1,441.8L626.1,441.9L632.1,441.3L635.2,443.8L639.5,444.5L642.6,442.7L642.7,441.3L649.6,441.0L656.2,440.9L651.5,442.6L653.4,445.2L657.8,445.6L662.0,448.3L662.9,452.8L665.8,452.7L668.0,454.0L663.6,457.2L663.1,459.3L665.0,461.3L663.6,462.4L660.2,463.3L660.3,465.8L658.8,467.4L662.6,471.6Z",
  "YE": "M1306.7,374.2L1309.3,378.2L1305.6,389.3L1288.9,394.8L1240.1,407.8L1239.5,405.5L1241.0,402.7L1243.3,404.2L1244.8,403.7L1251.2,403.5L1252.2,404.1L1257.6,404.7L1259.7,404.4L1261.1,406.2L1263.7,405.3L1267.7,399.5L1272.9,397.0L1288.9,394.8L1271.2,346.5L1273.9,347.8L1274.8,349.7L1278.6,352.1L1279.0,354.4L1278.4,356.2L1279.1,358.1L1280.7,359.6L1281.5,361.5L1282.3,362.8Z",
  "AF": "M1369.9,333.8h-5.4l-3.8-0.5l-2.5,2.9l-2.1,0.7l-1.5,1.3l-2.6-2.1l-1-5.4l-1.6-0.3v-2l-3.2-1.5l-1.7,2.3l0.2,2.6 l-0.6,0.9l-3.2-0.1l-0.9,3l-2.1-1.3l-3.3,2.1l-1.8-0.8l-4.3-1.4h-2.9l-1.6-0.2l-2.9-1.7l-0.3,2.3l-4.1,1.2l0.1,5.2l-2.5,2l-4,0.9 l-0.4,3l-3.9,0.8l-5.9-2.4l-0.5,8l-0.5,4.7l2.5,0.9l-1.6,3.5l2.7,5.1l1.1,4l4.3,1.1l1.1,4l-3.9,5.8l9.6,3.2l5.3-0.9l3.3,0.8l0.9-1.4 l3.8,0.5l6.6-2.6l-0.8-5.4l2.3-3.6h4l0.2-1.7l4-0.9l2.1,0.6l1.7-1.8l-1.1-3.8l1.5-3.8l3-1.6l-3-4.2l5.1,0.2l0.9-2.3l-0.8-2.5l2-2.7 l-1.4-3.2l-1.9-2.8l2.4-2.8l5.3-1.3l5.8-0.8l2.4-1.2l2.8-0.7L1369.9,333.8L1369.9,333.8z",
  "CM": "M1060.1,502.9l0.2-4.3l-0.5-4.2l-2.2-4.1l-1.6,0.4l-0.2,2l2.3,2.6l-0.6,1.1l-0.3,2.1l-4.6,5l-1.5,4l-0.7,3.3 l-1.2,1.4l-1.1,4.5l-3,2.6l-0.8,3.2l-1.2,2.6l-0.5,2.6l-3.9,2.2l-3.2-2.6l-2.1,0.1l-3.3,3.7l-1.6,0.1l-2.7,6.1l-1.4,4.5v1.8l1.4,0.9 l1.1,2.8l2.6,1.1l2.2,4.2l-0.8,5l9.2,0.2l2.6-0.4l3.4,0.8l3.4-0.8l0.7,0.3l7.1,0.3l4.5,1.7l4.5,1.5l0.4-3.5l-0.6-1.8l-0.3-2.9 l-2.6-2.1l-2.1-3.2l-0.5-2.3l-2.6-3.3l0.4-1.9l-0.6-2.7l0.4-5l1.4-1.1l2.7-6.5l0.9-1.7l-1.8-4.4l-0.8-2.6l-2.5-1.1l-3.3-3.7l1.2-3 l2.5,0.6l1.6-0.4l3.1,0.1L1060.1,502.9L1060.1,502.9z",
  "PY": "M655.7,700.5l-0.3-1.9l-5.4-3.3l-5.1-0.1l-9.5,1.9l-2.1,5.6l0.2,3.4l-1.5,7.6l11.2,10.4l4.6,1l7.2,4.7l5.9,2.5 l1.1,2.8l-4.2,9.6l5.7,1.8l6.2,1l4.2-1.1l4.3-4.8l0.3-5.7l0.7-3.6l0.3-3.8l-0.3-3.5l-2.1-1.2l-2,1.1l-2-0.3l-0.9-2.5l-1-5.8 l-1.2-1.9l-3.9-1.7l-2.1,1.2l-6-1.2l-0.4-8.6L655.7,700.5L655.7,700.5z",
  "UA": "M1138.5,241l-4.8,0.5l-1.5-0.3l-1,1.4l-1.8-0.2l0,0l-4.1,0.3l-1.2,1.4l0.2,3.1l-2-0.6l-4.3,0.3l-1.5-1.5l-1.6,1.1 l-2-0.9l-3.8-0.1l-5.6-1.5l-5-0.5l-3.7,0.2l-2.4,1.6l-2.2,0.3l3.1,5.3l-0.3,1.8l-2.3,0.7l-3.8,5.1l1.6,2.8l-1.1-0.4l-1.1,1.7 l-0.7,2.5l2.9,1.7l0.6,1.6l1.9-1.3l3.2,0.7h3.2l2.4,1.5l1.6-0.9l3.6-0.6l1-1.5h2.1l1.1-0.9l3.2-0.6l3.9,1.9l2,0.3l2.5,1.6v2.1 l1.9,1.1l1.1,2.6l2,1.5l-0.2,1l1,0.6l-1.2,0.5l-3-0.2l-0.6-0.9l-1,0.5l0.5,1.1l-1.1,2l-0.5,2.1l-1.2,0.7l2.4,1.1l2.2-1l2.4,1.1 l3.3-4.6l1.3-3.4l4.5-0.8l0.7,2.4l8,1.5l1.7,1.4l-4.5,2.1l-0.7,1.2l5.8,1.8l-0.6,2.9l3,1.3l6.3-3.6l5.3-1.1l0.6-2.2l-5.1,0.4 l-2.7-1.5l-1-3.9l3.9-2.3l4.6-0.3l3-2l3.9-0.5l-0.4-2.8l2.2-1.7l4.7-0.5l0.3-2.1l-1.8-3.4l1.3-3.2l-0.4-1.9l-7.6-2l-2.9,0.1 l-3.6-2.9l-3.5,1l-6.6-2.2l-0.2-1.2l-2.2-2.7l-4-0.2l-0.7-1.9l0.9-1.3L1138.5,241L1138.5,241z"
};

const WORLD_MAP_MARKERS = {"vatican": {"x": 1042, "y": 320}};
const WORLD_MAP_EXTRA_MARKERS = {"ad": {"x": 1008.4, "y": 264.2}, "ag": {"x": 656.4, "y": 405.2}, "al": {"x": 1110.1, "y": 270.7}, "am": {"x": 1247.3, "y": 277.1}, "ao": {"x": 1073.5, "y": 549.7}, "az": {"x": 1277.1, "y": 275.8}, "bb": {"x": 668.8, "y": 427.6}, "bd": {"x": 1502.3, "y": 368.1}, "bf": {"x": 991.5, "y": 431.7}, "bg": {"x": 1129.6, "y": 263.0}, "bh": {"x": 1281.1, "y": 354.6}, "bi": {"x": 1163.1, "y": 519.2}, "bj": {"x": 1013.4, "y": 465.1}, "bn": {"x": 1638.6, "y": 473.0}, "bs": {"x": 570.3, "y": 361.1}, "bt": {"x": 1498.0, "y": 347.7}, "by": {"x": 1153.2, "y": 200.8}, "cd": {"x": 1084.8, "y": 525.2}, "cf": {"x": 1103.1, "y": 476.1}, "cg": {"x": 1084.9, "y": 524.2}, "ci": {"x": 970.7, "y": 462.5}, "cu": {"x": 542.3, "y": 371.9}, "cy": {"x": 1185.3, "y": 304.9}, "dj": {"x": 1239.7, "y": 436.0}, "dm": {"x": 658.9, "y": 415.4}, "do": {"x": 611.5, "y": 397.7}, "dz": {"x": 1017.0, "y": 296.1}, "ee": {"x": 1137.5, "y": 169.9}, "er": {"x": 1216.3, "y": 415.3}, "et": {"x": 1215.2, "y": 450.3}, "fi": {"x": 1138.6, "y": 165.9}, "fm": {"x": 1878.6, "y": 462.0}, "ga": {"x": 1052.5, "y": 498.2}, "gd": {"x": 656.9, "y": 433.5}, "gh": {"x": 998.9, "y": 469.4}, "gm": {"x": 907.9, "y": 425.7}, "gn": {"x": 923.8, "y": 447.6}, "gq": {"x": 1048.8, "y": 479.6}, "gt": {"x": 497.2, "y": 419.1}, "gw": {"x": 913.3, "y": 434.5}, "gy": {"x": 676.9, "y": 462.7}, "hn": {"x": 515.4, "y": 422.1}, "ht": {"x": 598.3, "y": 397.1}, "hu": {"x": 1105.8, "y": 236.3}, "il": {"x": 1195.6, "y": 323.8}, "jm": {"x": 573.3, "y": 400.3}, "ki": {"x": 1961.2, "y": 492.4}, "km": {"x": 1240.3, "y": 565.6}, "kn": {"x": 651.5, "y": 404.3}, "lc": {"x": 661.2, "y": 422.6}, "md": {"x": 1160.3, "y": 239.1}, "me": {"x": 1107.0, "y": 264.5}, "mh": {"x": 1952.1, "y": 461.0}, "mm": {"x": 1534.1, "y": 390.7}, "mn": {"x": 1594.0, "y": 234.0}, "mv": {"x": 1408.4, "y": 477.3}, "mz": {"x": 1180.9, "y": 644.9}, "nr": {"x": 1927.3, "y": 503.6}, "pk": {"x": 1405.8, "y": 313.2}, "pw": {"x": 1747.1, "y": 459.7}, "ru": {"x": 1209.0, "y": 190.5}, "sb": {"x": 1888.6, "y": 552.9}, "sc": {"x": 1308.1, "y": 526.2}, "sn": {"x": 902.9, "y": 418.6}, "sv": {"x": 504.3, "y": 424.4}, "sy": {"x": 1201.6, "y": 314.1}, "td": {"x": 1083.7, "y": 433.0}, "tj": {"x": 1382.2, "y": 286.1}, "to": {"x": 26.7, "y": 618.1}, "tv": {"x": 1995.6, "y": 547.9}, "tw": {"x": 1675.4, "y": 361.3}, "vc": {"x": 659.9, "y": 427.3}, "ws": {"x": 45.8, "y": 577.4}};
const WORLD_MAP_EXTRA_META = {
  "ad": { nameEn: "Andorra", namePt: "Andorra", contEn: "Europe", contPt: "Europa" },
  "af": { nameEn: "Afghanistan", namePt: "Afeganistão", contEn: "Asia", contPt: "Ásia" },
  "ag": { nameEn: "Antigua and Barbuda", namePt: "Antígua e Barbuda", contEn: "North America", contPt: "América do Norte" },
  "al": { nameEn: "Albania", namePt: "Albânia", contEn: "Europe", contPt: "Europa" },
  "am": { nameEn: "Armenia", namePt: "Arménia", contEn: "Asia", contPt: "Ásia" },
  "ao": { nameEn: "Angola", namePt: "Angola", contEn: "Africa", contPt: "África" },
  "az": { nameEn: "Azerbaijan", namePt: "Azerbaijão", contEn: "Asia", contPt: "Ásia" },
  "bb": { nameEn: "Barbados", namePt: "Barbados", contEn: "North America", contPt: "América do Norte" },
  "bd": { nameEn: "Bangladesh", namePt: "Bangladesh", contEn: "Asia", contPt: "Ásia" },
  "bf": { nameEn: "Burkina Faso", namePt: "Burquina Faso", contEn: "Africa", contPt: "África" },
  "bg": { nameEn: "Bulgaria", namePt: "Bulgária", contEn: "Europe", contPt: "Europa" },
  "bh": { nameEn: "Bahrain", namePt: "Barém", contEn: "Asia", contPt: "Ásia" },
  "bi": { nameEn: "Burundi", namePt: "Burundi", contEn: "Africa", contPt: "África" },
  "bj": { nameEn: "Benin", namePt: "Benim", contEn: "Africa", contPt: "África" },
  "bn": { nameEn: "Brunei", namePt: "Brunei", contEn: "Asia", contPt: "Ásia" },
  "bs": { nameEn: "Bahamas", namePt: "Baamas", contEn: "North America", contPt: "América do Norte" },
  "bt": { nameEn: "Bhutan", namePt: "Butão", contEn: "Asia", contPt: "Ásia" },
  "by": { nameEn: "Belarus", namePt: "Bielorrússia", contEn: "Europe", contPt: "Europa" },
  "cd": { nameEn: "DR Congo", namePt: "RD Congo", contEn: "Africa", contPt: "África" },
  "cf": { nameEn: "Central African Republic", namePt: "República Centro-Africana", contEn: "Africa", contPt: "África" },
  "cg": { nameEn: "Republic of the Congo", namePt: "República do Congo", contEn: "Africa", contPt: "África" },
  "ci": { nameEn: "Côte d'Ivoire", namePt: "Costa do Marfim", contEn: "Africa", contPt: "África" },
  "cm": { nameEn: "Cameroon", namePt: "Camarões", contEn: "Africa", contPt: "África" },
  "cu": { nameEn: "Cuba", namePt: "Cuba", contEn: "North America", contPt: "América do Norte" },
  "cy": { nameEn: "Cyprus", namePt: "Chipre", contEn: "Europe", contPt: "Europa" },
  "dj": { nameEn: "Djibouti", namePt: "Jibuti", contEn: "Africa", contPt: "África" },
  "dm": { nameEn: "Dominica", namePt: "Dominica", contEn: "North America", contPt: "América do Norte" },
  "do": { nameEn: "Dominican Republic", namePt: "República Dominicana", contEn: "North America", contPt: "América do Norte" },
  "dz": { nameEn: "Algeria", namePt: "Argélia", contEn: "Africa", contPt: "África" },
  "ee": { nameEn: "Estonia", namePt: "Estónia", contEn: "Europe", contPt: "Europa" },
  "er": { nameEn: "Eritrea", namePt: "Eritreia", contEn: "Africa", contPt: "África" },
  "et": { nameEn: "Ethiopia", namePt: "Etiópia", contEn: "Africa", contPt: "África" },
  "fi": { nameEn: "Finland", namePt: "Finlândia", contEn: "Europe", contPt: "Europa" },
  "fm": { nameEn: "Micronesia", namePt: "Micronésia", contEn: "Oceania", contPt: "Oceânia" },
  "ga": { nameEn: "Gabon", namePt: "Gabão", contEn: "Africa", contPt: "África" },
  "gd": { nameEn: "Grenada", namePt: "Granada", contEn: "North America", contPt: "América do Norte" },
  "gh": { nameEn: "Ghana", namePt: "Gana", contEn: "Africa", contPt: "África" },
  "gm": { nameEn: "Gambia", namePt: "Gâmbia", contEn: "Africa", contPt: "África" },
  "gn": { nameEn: "Guinea", namePt: "Guiné", contEn: "Africa", contPt: "África" },
  "gq": { nameEn: "Equatorial Guinea", namePt: "Guiné Equatorial", contEn: "Africa", contPt: "África" },
  "gt": { nameEn: "Guatemala", namePt: "Guatemala", contEn: "North America", contPt: "América do Norte" },
  "gw": { nameEn: "Guinea-Bissau", namePt: "Guiné-Bissau", contEn: "Africa", contPt: "África" },
  "gy": { nameEn: "Guyana", namePt: "Guiana", contEn: "South America", contPt: "América do Sul" },
  "hn": { nameEn: "Honduras", namePt: "Honduras", contEn: "North America", contPt: "América do Norte" },
  "ht": { nameEn: "Haiti", namePt: "Haiti", contEn: "North America", contPt: "América do Norte" },
  "hu": { nameEn: "Hungary", namePt: "Hungria", contEn: "Europe", contPt: "Europa" },
  "il": { nameEn: "Israel", namePt: "Israel", contEn: "Asia", contPt: "Ásia" },
  "iq": { nameEn: "Iraq", namePt: "Iraque", contEn: "Asia", contPt: "Ásia" },
  "ir": { nameEn: "Iran", namePt: "Irão", contEn: "Asia", contPt: "Ásia" },
  "jm": { nameEn: "Jamaica", namePt: "Jamaica", contEn: "North America", contPt: "América do Norte" },
  "jo": { nameEn: "Jordan", namePt: "Jordânia", contEn: "Asia", contPt: "Ásia" },
  "kg": { nameEn: "Kyrgyzstan", namePt: "Quirguistão", contEn: "Asia", contPt: "Ásia" },
  "ki": { nameEn: "Kiribati", namePt: "Quiribati", contEn: "Oceania", contPt: "Oceânia" },
  "km": { nameEn: "Comoros", namePt: "Comores", contEn: "Africa", contPt: "África" },
  "kn": { nameEn: "St Kitts and Nevis", namePt: "São Cristóvão e Neves", contEn: "North America", contPt: "América do Norte" },
  "kp": { nameEn: "North Korea", namePt: "Coreia do Norte", contEn: "Asia", contPt: "Ásia" },
  "kr": { nameEn: "South Korea", namePt: "Coreia do Sul", contEn: "Asia", contPt: "Ásia" },
  "kz": { nameEn: "Kazakhstan", namePt: "Cazaquistão", contEn: "Asia", contPt: "Ásia" },
  "lb": { nameEn: "Lebanon", namePt: "Líbano", contEn: "Asia", contPt: "Ásia" },
  "lc": { nameEn: "St Lucia", namePt: "Santa Lúcia", contEn: "North America", contPt: "América do Norte" },
  "lk": { nameEn: "Sri Lanka", namePt: "Sri Lanka", contEn: "Asia", contPt: "Ásia" },
  "lr": { nameEn: "Liberia", namePt: "Libéria", contEn: "Africa", contPt: "África" },
  "ls": { nameEn: "Lesotho", namePt: "Lesoto", contEn: "Africa", contPt: "África" },
  "lt": { nameEn: "Lithuania", namePt: "Lituânia", contEn: "Europe", contPt: "Europa" },
  "lv": { nameEn: "Latvia", namePt: "Letónia", contEn: "Europe", contPt: "Europa" },
  "ly": { nameEn: "Libya", namePt: "Líbia", contEn: "Africa", contPt: "África" },
  "md": { nameEn: "Moldova", namePt: "Moldávia", contEn: "Europe", contPt: "Europa" },
  "me": { nameEn: "Montenegro", namePt: "Montenegro", contEn: "Europe", contPt: "Europa" },
  "mg": { nameEn: "Madagascar", namePt: "Madagáscar", contEn: "Africa", contPt: "África" },
  "mh": { nameEn: "Marshall Islands", namePt: "Ilhas Marshall", contEn: "Oceania", contPt: "Oceânia" },
  "ml": { nameEn: "Mali", namePt: "Mali", contEn: "Africa", contPt: "África" },
  "mm": { nameEn: "Myanmar", namePt: "Myanmar", contEn: "Asia", contPt: "Ásia" },
  "mn": { nameEn: "Mongolia", namePt: "Mongólia", contEn: "Asia", contPt: "Ásia" },
  "mr": { nameEn: "Mauritania", namePt: "Mauritânia", contEn: "Africa", contPt: "África" },
  "mt": { nameEn: "Malta", namePt: "Malta", contEn: "Europe", contPt: "Europa" },
  "mv": { nameEn: "Maldives", namePt: "Maldivas", contEn: "Asia", contPt: "Ásia" },
  "mw": { nameEn: "Malawi", namePt: "Maláui", contEn: "Africa", contPt: "África" },
  "mz": { nameEn: "Mozambique", namePt: "Moçambique", contEn: "Africa", contPt: "África" },
  "ne": { nameEn: "Niger", namePt: "Níger", contEn: "Africa", contPt: "África" },
  "ng": { nameEn: "Nigeria", namePt: "Nigéria", contEn: "Africa", contPt: "África" },
  "ni": { nameEn: "Nicaragua", namePt: "Nicarágua", contEn: "North America", contPt: "América do Norte" },
  "np": { nameEn: "Nepal", namePt: "Nepal", contEn: "Asia", contPt: "Ásia" },
  "nr": { nameEn: "Nauru", namePt: "Nauru", contEn: "Oceania", contPt: "Oceânia" },
  "pg": { nameEn: "Papua New Guinea", namePt: "Papua-Nova Guiné", contEn: "Oceania", contPt: "Oceânia" },
  "ph": { nameEn: "Philippines", namePt: "Filipinas", contEn: "Asia", contPt: "Ásia" },
  "pk": { nameEn: "Pakistan", namePt: "Paquistão", contEn: "Asia", contPt: "Ásia" },
  "ps": { nameEn: "Palestine", namePt: "Palestina", contEn: "Asia", contPt: "Ásia" },
  "pw": { nameEn: "Palau", namePt: "Palau", contEn: "Oceania", contPt: "Oceânia" },
  "py": { nameEn: "Paraguay", namePt: "Paraguai", contEn: "South America", contPt: "América do Sul" },
  "ro": { nameEn: "Romania", namePt: "Roménia", contEn: "Europe", contPt: "Europa" },
  "ru": { nameEn: "Russia", namePt: "Rússia", contEn: "Europe", contPt: "Europa" },
  "rw": { nameEn: "Rwanda", namePt: "Ruanda", contEn: "Africa", contPt: "África" },
  "sa": { nameEn: "Saudi Arabia", namePt: "Arábia Saudita", contEn: "Asia", contPt: "Ásia" },
  "sb": { nameEn: "Solomon Islands", namePt: "Ilhas Salomão", contEn: "Oceania", contPt: "Oceânia" },
  "sc": { nameEn: "Seychelles", namePt: "Seicheles", contEn: "Africa", contPt: "África" },
  "sd": { nameEn: "Sudan", namePt: "Sudão", contEn: "Africa", contPt: "África" },
  "si": { nameEn: "Slovenia", namePt: "Eslovénia", contEn: "Europe", contPt: "Europa" },
  "sl": { nameEn: "Sierra Leone", namePt: "Serra Leoa", contEn: "Africa", contPt: "África" },
  "sn": { nameEn: "Senegal", namePt: "Senegal", contEn: "Africa", contPt: "África" },
  "so": { nameEn: "Somalia", namePt: "Somália", contEn: "Africa", contPt: "África" },
  "sr": { nameEn: "Suriname", namePt: "Suriname", contEn: "South America", contPt: "América do Sul" },
  "ss": { nameEn: "South Sudan", namePt: "Sudão do Sul", contEn: "Africa", contPt: "África" },
  "st": { nameEn: "São Tomé and Príncipe", namePt: "São Tomé e Príncipe", contEn: "Africa", contPt: "África" },
  "sv": { nameEn: "El Salvador", namePt: "El Salvador", contEn: "North America", contPt: "América do Norte" },
  "sy": { nameEn: "Syria", namePt: "Síria", contEn: "Asia", contPt: "Ásia" },
  "sz": { nameEn: "Eswatini", namePt: "Essuatíni", contEn: "Africa", contPt: "África" },
  "td": { nameEn: "Chad", namePt: "Chade", contEn: "Africa", contPt: "África" },
  "tg": { nameEn: "Togo", namePt: "Togo", contEn: "Africa", contPt: "África" },
  "tj": { nameEn: "Tajikistan", namePt: "Tajiquistão", contEn: "Asia", contPt: "Ásia" },
  "tl": { nameEn: "Timor-Leste", namePt: "Timor-Leste", contEn: "Asia", contPt: "Ásia" },
  "tm": { nameEn: "Turkmenistan", namePt: "Turquemenistão", contEn: "Asia", contPt: "Ásia" },
  "tn": { nameEn: "Tunisia", namePt: "Tunísia", contEn: "Africa", contPt: "África" },
  "to": { nameEn: "Tonga", namePt: "Tonga", contEn: "Oceania", contPt: "Oceânia" },
  "tt": { nameEn: "Trinidad and Tobago", namePt: "Trindade e Tobago", contEn: "North America", contPt: "América do Norte" },
  "tv": { nameEn: "Tuvalu", namePt: "Tuvalu", contEn: "Oceania", contPt: "Oceânia" },
  "tw": { nameEn: "Taiwan", namePt: "Taiwan", contEn: "Asia", contPt: "Ásia" },
  "ua": { nameEn: "Ukraine", namePt: "Ucrânia", contEn: "Europe", contPt: "Europa" },
  "ug": { nameEn: "Uganda", namePt: "Uganda", contEn: "Africa", contPt: "África" },
  "uy": { nameEn: "Uruguay", namePt: "Uruguai", contEn: "South America", contPt: "América do Sul" },
  "uz": { nameEn: "Uzbekistan", namePt: "Usbequistão", contEn: "Asia", contPt: "Ásia" },
  "vc": { nameEn: "St Vincent and the Grenadines", namePt: "São Vicente e Granadinas", contEn: "North America", contPt: "América do Norte" },
  "ve": { nameEn: "Venezuela", namePt: "Venezuela", contEn: "South America", contPt: "América do Sul" },
  "ws": { nameEn: "Samoa", namePt: "Samoa", contEn: "Oceania", contPt: "Oceânia" },
  "ye": { nameEn: "Yemen", namePt: "Iémen", contEn: "Asia", contPt: "Ásia" }
};

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
  const [mapZoom, setMapZoom] = useState(1);
  const [mapPan, setMapPan] = useState({ x: 0, y: 0 });
  const [popoverCountry, setPopoverCountry] = useState(null);
  const [cameFromMap, setCameFromMap] = useState(false);
  const mapDragRef = useRef({ dragging: false, moved: false, startX: 0, startY: 0, panStartX: 0, panStartY: 0 });
  const [trips, setTrips] = useState({});
  const [activeTripId, setActiveTripId] = useState(null);
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
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [shareCopied, setShareCopied] = useState(false);
  const [sharedTrip, setSharedTrip] = useState(null);
  const [sharedTripStatus, setSharedTripStatus] = useState("idle");

  const normalize = (s) => (s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  const T = UI_STRINGS[lang];
  const continents = CONTINENTS.map((c) => localizeContinent(c, lang));
  const continent = continents.find((c) => c.id === continentId) || null;
  const country = continent ? continent.countries.find((c) => c.id === countryId) : null;

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

  const allCountriesFlat = continents.flatMap((c) => c.countries.map((cty) => ({ ...cty, continentId: c.id, continentName: c.name, continentColor: c.color })));
  const isoToFlag = (iso) => iso.toUpperCase().replace(/./g, (ch) => String.fromCodePoint(127397 + ch.charCodeAt(0)));
  const allCountriesForMap = allCountriesFlat.concat(
    Object.keys(WORLD_MAP_EXTRA_META).map((key) => {
      const m = WORLD_MAP_EXTRA_META[key];
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
  const totalAttractions = allCountriesFlat.reduce((sum, cty) => sum + (cty.attractions ? cty.attractions.length : 0), 0);
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

  const MAP_ZOOM_MAX = 6;
  const clampPan = (pan, zoom) => {
    const maxX = (zoom - 1) * 260;
    const maxY = (zoom - 1) * 140;
    return { x: Math.max(-maxX, Math.min(maxX, pan.x)), y: Math.max(-maxY, Math.min(maxY, pan.y)) };
  };
  const mapZoomIn = () => setMapZoom((z) => Math.min(MAP_ZOOM_MAX, +(z + 0.6).toFixed(2)));
  const mapZoomOut = () => setMapZoom((z) => {
    const nz = Math.max(1, +(z - 0.6).toFixed(2));
    if (nz === 1) setMapPan({ x: 0, y: 0 });
    else setMapPan((p) => clampPan(p, nz));
    return nz;
  });
  const mapZoomReset = () => { setMapZoom(1); setMapPan({ x: 0, y: 0 }); };
  const handleMapWheel = (e) => {
    e.preventDefault();
    const delta = e.deltaY > 0 ? -0.35 : 0.35;
    setMapZoom((z) => {
      const nz = Math.min(MAP_ZOOM_MAX, Math.max(1, +(z + delta).toFixed(2)));
      if (nz === 1) setMapPan({ x: 0, y: 0 });
      return nz;
    });
  };
  const handleMapPointerDown = (e) => {
    mapDragRef.current = { dragging: true, moved: false, startX: e.clientX, startY: e.clientY, panStartX: mapPan.x, panStartY: mapPan.y };
  };
  const handleMapPointerMove = (e) => {
    if (!mapDragRef.current.dragging) return;
    const dx = e.clientX - mapDragRef.current.startX;
    const dy = e.clientY - mapDragRef.current.startY;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) mapDragRef.current.moved = true;
    if (mapZoom > 1) setMapPan(clampPan({ x: mapDragRef.current.panStartX + dx, y: mapDragRef.current.panStartY + dy }, mapZoom));
  };
  const handleMapPointerUp = () => { mapDragRef.current.dragging = false; };
  const handleMapCountryClick = (cty) => {
    if (mapDragRef.current.moved) return;
    goToDetailFromMap(cty);
  };

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

  const exportTripPDF = (trip) => {
    if (!window.jspdf) return;
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    const pageWidth = doc.internal.pageSize.getWidth();
    const margin = 15;
    const navy = [20, 32, 53];
    const gold = [184, 134, 62];
    const inkSoft = [131, 121, 95];
    const ink = [31, 27, 20];
    const hairline = [225, 214, 188];

    doc.setFillColor(navy[0], navy[1], navy[2]);
    doc.rect(0, 0, pageWidth, 34, "F");
    doc.setDrawColor(255, 255, 255);
    doc.circle(margin + 5, 17, 5, "S");
    doc.setFillColor(gold[0], gold[1], gold[2]);
    doc.circle(margin + 5, 17, 2, "F");
    doc.setFontSize(11);
    doc.setTextColor(255, 255, 255);
    doc.text("WAYPOINT", margin + 15, 14);
    doc.setFontSize(18);
    doc.text(trip.name, margin + 15, 25);

    let y = 46;
    doc.setFontSize(10);
    doc.setTextColor(inkSoft[0], inkSoft[1], inkSoft[2]);
    doc.text((trip.startDate || "?") + " - " + (trip.endDate || "?") + "  ·  " + dayCount(trip.startDate, trip.endDate) + " " + T.days, margin, y);
    y += 10;

    trip.stops.forEach((stop) => {
      const maxTextWidth = pageWidth - margin * 2 - 14;
      const noteDays = Array.from({ length: Math.max(1, stop.dayEnd - stop.dayStart + 1) }, (_, di) => stop.dayStart + di)
        .filter((day) => ((trip.dailyNotes || {})[day] || "").trim());
      let noteLinesTotal = 0;
      const wrappedNotes = noteDays.map((day) => {
        const text = String(trip.dailyNotes[day]).trim();
        const wrapped = doc.splitTextToSize(text, maxTextWidth);
        noteLinesTotal += 1 + wrapped.length;
        return { day, wrapped };
      });

      const lineCount = stop.highlights.length + (stop.stays || []).length + (stop.meals || []).length
        + noteLinesTotal + (noteDays.length > 0 ? 3 : 0);
      const boxHeight = 16 + lineCount * 5.5;
      if (y + boxHeight > 275) { doc.addPage(); y = 20; }

      doc.setDrawColor(hairline[0], hairline[1], hairline[2]);
      doc.setLineWidth(0.4);
      doc.roundedRect(margin, y, pageWidth - margin * 2, boxHeight, 3, 3, "S");

      let iy = y + 10;
      doc.setFontSize(13);
      doc.setTextColor(ink[0], ink[1], ink[2]);
      doc.text(stop.city || T.cityPlaceholder, margin + 6, iy);
      doc.setFontSize(9);
      doc.setTextColor(inkSoft[0], inkSoft[1], inkSoft[2]);
      doc.text(T.day + " " + stop.dayStart + "-" + stop.dayEnd, pageWidth - margin - 6, iy, { align: "right" });
      iy += 7;

      doc.setFontSize(10);
      doc.setTextColor(60, 55, 45);
      stop.highlights.forEach((h) => { doc.text("- " + h.text, margin + 8, iy); iy += 5.5; });
      (stop.stays || []).forEach((st) => { doc.text(T.whereToSleep + ": " + st.name + (st.nights ? " (" + st.nights + " " + T.nights + ")" : "") + (st.price ? " - " + st.price : ""), margin + 8, iy); iy += 5.5; });
      (stop.meals || []).forEach((m) => { doc.text(T.whereToEat + ": " + m.name, margin + 8, iy); iy += 5.5; });

      if (noteDays.length > 0) {
        iy += 2;
        doc.setDrawColor(hairline[0], hairline[1], hairline[2]);
        doc.setLineWidth(0.2);
        doc.line(margin + 6, iy - 3.5, pageWidth - margin - 6, iy - 3.5);
        doc.setFont("helvetica", "bold");
        doc.setFontSize(8);
        doc.setTextColor(gold[0], gold[1], gold[2]);
        doc.text(T.dayNotes.toUpperCase(), margin + 6, iy);
        doc.setFont("helvetica", "normal");
        iy += 5.5;
        wrappedNotes.forEach(({ day, wrapped }) => {
          doc.setFont("helvetica", "bold");
          doc.setFontSize(9);
          doc.setTextColor(ink[0], ink[1], ink[2]);
          doc.text(T.day + " " + day, margin + 8, iy);
          iy += 5;
          doc.setFont("helvetica", "italic");
          doc.setFontSize(9.5);
          doc.setTextColor(70, 64, 52);
          wrapped.forEach((line) => { doc.text(line, margin + 10, iy); iy += 4.6; });
          doc.setFont("helvetica", "normal");
          iy += 2;
        });
      }

      y += boxHeight + 4;

      const transit = trip.transits.find((tr) => tr.afterStopId === stop.id);
      if (transit && transit.mode) {
        const durTxt = (transit.durationHours || transit.durationMinutes) ? " · " + (transit.durationHours || 0) + "h" + (transit.durationMinutes ? transit.durationMinutes + "m" : "") : "";
        doc.setFontSize(9);
        doc.setTextColor(gold[0], gold[1], gold[2]);
        doc.text(transit.mode.toUpperCase() + durTxt + (transit.price ? " · " + transit.price : ""), margin + 6, y);
        y += 8;
      }
    });

    y += 3;
    doc.setDrawColor(hairline[0], hairline[1], hairline[2]);
    doc.line(margin, y, pageWidth - margin, y);
    y += 9;
    doc.setFontSize(12);
    doc.setTextColor(ink[0], ink[1], ink[2]);
    doc.text(T.estimatedCost + ": EUR " + tripTotalCost(trip).toFixed(0), margin, y);
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
        @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Work+Sans:wght@400;500;600&display=swap');
        .wp-root {
          --parchment: #F6F2E8; --ink: #1F1B14; --ink-soft: #83795F; --hairline: #E1D6BC; --navy: #142035; --gold: #B8863E;
          font-family: 'Work Sans', sans-serif; background: var(--parchment); color: var(--ink);
          min-height: 100vh; width: 100%; box-sizing: border-box;
          padding: calc(env(safe-area-inset-top, 0px) + 1.75rem) 1.25rem 4rem;
        }
        .wp-root * { box-sizing: border-box; }
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
        .wp-title { font-family: 'Fraunces', serif; font-size: 2rem; font-weight: 600; letter-spacing: -0.01em; margin: 0; }
        .wp-hero-headline { font-family: 'Fraunces', serif; font-size: 2.6rem; font-weight: 600; letter-spacing: -0.02em; line-height: 1.04; margin: 0 0 0.9rem; }
        @media (min-width: 600px) { .wp-hero-headline { font-size: 3.1rem; } }
        .wp-tagline { font-size: 0.96rem; color: var(--ink-soft); margin: 0 0 1.1rem; max-width: 54ch; line-height: 1.5; }
        .wp-hero-stats { display: flex; gap: 1.7rem; margin-bottom: 1.4rem; }
        .wp-hero-stat b { font-family: 'Fraunces', serif; font-size: 1.4rem; font-weight: 600; display: block; line-height: 1.2; }
        .wp-hero-stat span { font-size: 0.76rem; color: var(--ink-soft); }
        .wp-hero-features { display: flex; flex-direction: column; gap: 0.6rem; max-width: 30rem; }
        .wp-hero-feature-card { display: flex; align-items: flex-start; gap: 0.7rem; text-align: left; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.7rem 0.9rem; cursor: pointer; color: var(--ink); }
        .wp-hero-feature-card:hover { border-color: var(--gold); }
        .wp-hero-feature-card svg { flex-shrink: 0; margin-top: 0.15rem; color: var(--gold); }
        .wp-hero-feature-card b { display: block; font-family: 'Fraunces', serif; font-size: 0.95rem; font-weight: 600; margin-bottom: 0.1rem; }
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
        .wp-continent-name { font-family: 'Fraunces', serif; font-size: 1.25rem; font-weight: 600; }
        .wp-continent-tagline { font-size: 0.82rem; color: var(--ink-soft); line-height: 1.35; margin-top: 0.2rem; }
        .wp-continent-count { font-family: 'Fraunces', serif; font-size: 0.95rem; color: var(--tile-color); }
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
        .wp-quiz-clue-text { font-family: 'Fraunces', serif; font-style: italic; font-size: 1.25rem; text-align: center; line-height: 1.4; color: var(--ink); }
        .wp-quiz-clue-food { font-size: 1.05rem; text-align: center; line-height: 1.5; }
        .wp-quiz-prompt { text-align: center; font-size: 0.9rem; color: var(--ink-soft); margin: 0 0 1.1rem; }
        .wp-quiz-options { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.6rem; }
        @media (max-width: 480px) { .wp-quiz-options { grid-template-columns: 1fr; } }
        .wp-quiz-option { background: var(--parchment); border: 1px solid var(--hairline); border-radius: 3px; padding: 0.7rem 0.9rem; font-family: inherit; font-size: 0.92rem; cursor: pointer; text-align: left; display: flex; align-items: center; gap: 0.5rem; }
        .wp-quiz-option:hover:not(:disabled) { border-color: var(--navy); }
        .wp-quiz-option:disabled { cursor: default; }
        .wp-quiz-option-correct { background: #E4EFE2; border-color: #6B9E68; font-weight: 600; }
        .wp-quiz-option-wrong { background: #F5E2E0; border-color: #C1665F; }
        .wp-quiz-btn { background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.65rem 1.4rem; font-family: 'Work Sans', sans-serif; font-size: 0.9rem; font-weight: 600; cursor: pointer; color: var(--ink); display: inline-flex; align-items: center; gap: 0.4rem; }
        .wp-quiz-btn-primary { background: var(--navy); color: #F3EDE0; border-color: var(--navy); }
        .wp-quiz-score { font-family: 'Fraunces', serif; font-size: 2.6rem; font-weight: 600; margin: 0.5rem 0 0.15rem; color: #fff; }
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
        .wp-now-name { font-family: 'Fraunces', serif; font-size: 1.1rem; font-weight: 600; border-bottom: 2px solid transparent; display: inline-block; width: fit-content; transition: border-color 0.15s ease; }
        .wp-now-card:hover .wp-now-name { border-bottom-color: var(--gold); }
        .wp-now-reason { font-size: 0.85rem; color: #4a4436; line-height: 1.5; }

        .wp-search-wrap { margin-bottom: 1.3rem; }
        .wp-search-box { display: flex; align-items: center; gap: 0.65rem; background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.85rem 1.3rem; box-shadow: 0 1px 2px rgba(31,27,20,0.04); }
        .wp-search-icon { color: var(--ink-soft); flex-shrink: 0; }
        .wp-search-input { flex: 1; min-width: 0; border: none; outline: none; background: transparent; font-family: 'Work Sans', sans-serif; font-size: 0.95rem; color: var(--ink); }
        .wp-search-input::placeholder { color: var(--ink-soft); }
        .wp-search-clear { background: none; border: none; cursor: pointer; color: var(--ink-soft); padding: 0.15rem; display: flex; align-items: center; flex-shrink: 0; }
        .wp-search-clear:hover { color: var(--ink); }
        .wp-search-empty { font-size: 0.92rem; color: var(--ink-soft); padding: 0.6rem 0 1rem; }

        .wp-country-row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; width: 100%; background: #fff; border: 1px solid var(--hairline); border-left: 4px solid var(--row-color); border-radius: 2px; padding: 0.95rem 1.1rem; cursor: pointer; text-align: left; font-family: inherit; margin-bottom: 0.6rem; }
        .wp-country-row:hover { background: #FBF8F1; }
        .wp-country-name { font-family: 'Fraunces', serif; font-size: 1.08rem; font-weight: 500; display: flex; align-items: center; gap: 0.5rem; }
        .wp-country-capital { font-size: 0.82rem; color: var(--ink-soft); margin-top: 0.15rem; }

        .wp-detail-hero { margin-bottom: 1.6rem; }
        .wp-detail-name { font-family: 'Fraunces', serif; font-size: 2.1rem; font-weight: 600; margin: 0 0 0.2rem; letter-spacing: -0.01em; display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap; }
        .wp-detail-sub { font-size: 0.92rem; color: var(--ink-soft); }

        .wp-stat-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.1rem; background: #fff; border: 1px solid var(--hairline); border-radius: 3px; padding: 1.1rem 1.2rem; margin-bottom: 1.6rem; }
        @media (min-width: 520px) { .wp-stat-grid { grid-template-columns: repeat(4, 1fr); } }

        .wp-section-title { font-family: 'Fraunces', serif; font-size: 1.25rem; font-weight: 500; margin: 0 0 0.9rem; }
        .wp-blurb { font-size: 0.98rem; line-height: 1.6; margin-bottom: 1.9rem; max-width: 62ch; }

        .wp-attractions-grid { display: grid; grid-template-columns: 1fr; gap: 1.8rem; margin-bottom: 1.9rem; }
        @media (min-width: 620px) { .wp-attractions-grid { grid-template-columns: 1fr 1fr; } }
        .wp-attraction-img { width: 100%; height: 180px; object-fit: cover; border-radius: 8px; background: #EDE6D4; margin-bottom: 0.8rem; display: block; }
        .wp-attraction-img-loading { background: linear-gradient(90deg, #EDE6D4 25%, #F5F0E3 37%, #EDE6D4 63%); background-size: 400% 100%; animation: wp-shimmer 1.4s ease infinite; }
        @keyframes wp-shimmer { 0% { background-position: 100% 50%; } 100% { background-position: 0 50%; } }
        .wp-attraction-img-empty { display: flex; align-items: center; justify-content: center; }
        .wp-attraction-name { font-family: 'Fraunces', serif; font-weight: 600; font-size: 1.05rem; margin-bottom: 0.35rem; }
        .wp-attraction-desc { font-size: 0.88rem; color: #4a4436; line-height: 1.55; }

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
        .wp-day-title { font-family: 'Fraunces', serif; font-weight: 600; font-size: 1.12rem; margin-bottom: 0.3rem; }
        .wp-day-desc { font-size: 0.9rem; color: #4a4436; line-height: 1.5; }

        .wp-nav { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 0 0 1.3rem; border-bottom: 1px solid var(--hairline); margin-bottom: 1.6rem; flex-wrap: wrap; }
        .wp-nav-brand { display: flex; align-items: center; gap: 0.5rem; background: none; border: none; cursor: pointer; font-family: 'Fraunces', serif; font-size: 1.05rem; font-weight: 600; color: var(--ink); padding: 0; }
        .wp-nav-links { display: flex; gap: 1.4rem; flex-wrap: wrap; row-gap: 0.7rem; align-items: center; }
        @media (max-width: 680px) {
          .wp-nav-links { flex-basis: 100%; justify-content: center; gap: 0.7rem 0.9rem; margin-top: 0.7rem; }
        }
        .wp-nav-link { background: none; border: none; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.88rem; color: var(--ink-soft); padding: 0.3rem 0; border-bottom: 2px solid transparent; }
        .wp-nav-link:hover { color: var(--ink); }
        .wp-nav-link-active { color: var(--ink); border-bottom-color: var(--navy); font-weight: 600; }
        .wp-lang-toggle { display: flex; align-items: center; gap: 0.3rem; padding-left: 1rem; border-left: 1px solid var(--hairline); }
        .wp-lang-btn { background: none; border: none; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.82rem; color: var(--ink-soft); padding: 0.2rem 0.15rem; }
        .wp-lang-btn:hover { color: var(--ink); }
        .wp-lang-btn-active { color: var(--ink); font-weight: 700; }
        .wp-lang-sep { color: var(--hairline); font-size: 0.8rem; }

        .wp-signin-btn { background: var(--navy); color: #F6F2E8; border: none; border-radius: 999px; padding: 0.45rem 1rem; font-family: 'Work Sans', sans-serif; font-size: 0.85rem; font-weight: 600; cursor: pointer; }
        .wp-user-menu-wrap { position: relative; }
        .wp-user-chip { display: inline-flex; align-items: center; gap: 0.4rem; background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.4rem 0.85rem; font-family: 'Work Sans', sans-serif; font-size: 0.82rem; color: var(--ink); cursor: pointer; }
        .wp-user-dropdown { position: absolute; right: 0; top: calc(100% + 0.4rem); background: #fff; border: 1px solid var(--hairline); border-radius: 8px; box-shadow: 0 8px 20px rgba(31,27,20,0.12); padding: 0.4rem; min-width: 140px; z-index: 30; }
        .wp-user-dropdown-item { display: flex; align-items: center; gap: 0.5rem; width: 100%; background: none; border: none; text-align: left; padding: 0.5rem 0.6rem; border-radius: 5px; font-family: 'Work Sans', sans-serif; font-size: 0.85rem; color: var(--ink); cursor: pointer; }
        .wp-user-dropdown-item:hover { background: var(--parchment); }

        .wp-status-row { display: flex; gap: 0.6rem; margin-top: 0.9rem; }
        .wp-status-btn { display: inline-flex; align-items: center; gap: 0.4rem; background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.4rem 0.9rem; font-family: 'Work Sans', sans-serif; font-size: 0.82rem; font-weight: 600; color: var(--ink-soft); cursor: pointer; }
        .wp-status-btn:hover { border-color: var(--ink-soft); }
        .wp-status-visited.wp-status-active { background: #E4EFE9; border-color: #3F8F6F; color: #2E6B52; }
        .wp-status-want.wp-status-active { background: #FBF1DF; border-color: var(--gold); color: #8A6425; }

        .wp-status-dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-left: 0.5rem; vertical-align: middle; }
        .wp-status-dot-visited { background: #3F8F6F; }
        .wp-status-dot-want { background: var(--gold); }
        .wp-status-dot-none { background: #FFFFFF; border: 1px solid var(--hairline); box-sizing: border-box; }

        .wp-map-signin-banner { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; background: #fff; border: 1px solid var(--hairline); border-radius: 10px; padding: 0.9rem 1.2rem; margin-bottom: 1.2rem; font-size: 0.9rem; color: var(--ink-soft); }
        .wp-map-legend { display: flex; gap: 1.4rem; flex-wrap: wrap; margin-bottom: 1rem; font-size: 0.85rem; color: var(--ink-soft); }
        .wp-map-legend-item { display: inline-flex; align-items: center; }
        .wp-map-legend-item .wp-status-dot { margin-left: 0; margin-right: 0.45rem; }
        .wp-map-frame { position: relative; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.8rem; overflow: hidden; }
        .wp-world-map { width: 100%; height: auto; display: block; transform-origin: center center; }
        .wp-map-country { stroke: var(--hairline); stroke-width: 1; cursor: pointer; transition: opacity 0.12s ease, fill 0.12s ease, filter 0.12s ease; }
        .wp-map-country:hover { filter: brightness(1.08); }
        .wp-map-status-none { fill: #FFFFFF; }
        .wp-map-status-visited { fill: #3F8F6F; }
        .wp-map-status-want { fill: var(--gold); }
        .wp-map-marker { stroke: var(--hairline); stroke-width: 1.5; }
        .wp-map-status-none:hover { fill: #F6F2E8; }
        .wp-map-bg-country { fill: #FFFFFF; stroke: var(--hairline); stroke-width: 1; pointer-events: none; }
        .wp-map-bg-country.wp-map-clickable { pointer-events: auto; cursor: pointer; }
        .wp-map-bg-country.wp-map-clickable:hover { fill: #F6F2E8; }
        .wp-map-marker.wp-map-clickable { cursor: pointer; }

        .wp-map-progress-row { display: flex; align-items: center; gap: 1.2rem; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 1.2rem; }
        .wp-map-progress-stat { flex-shrink: 0; }
        .wp-map-progress-value { font-family: 'Fraunces', serif; font-size: 1.8rem; margin: 0; color: var(--ink); line-height: 1; }
        .wp-map-progress-label { font-size: 0.75rem; color: var(--ink-soft); margin: 0.2rem 0 0; }
        .wp-map-sparkline { flex: 1; height: 46px; min-width: 0; }

        .wp-map-zoom-controls { position: absolute; right: 1rem; bottom: 1rem; display: flex; flex-direction: column; gap: 0.3rem; }
        .wp-map-zoom-controls button { width: 32px; height: 32px; border-radius: 8px; background: #fff; border: 1px solid var(--hairline); color: var(--ink); cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
        .wp-map-zoom-controls button:hover { border-color: var(--gold); }
        .wp-map-zoom-reset { margin-top: 0.2rem; }

        .wp-map-popover { background: #fff; border-radius: 14px; padding: 1.3rem 1.4rem; max-width: 320px; width: 90%; position: relative; }
        .wp-map-popover-name { font-family: 'Fraunces', serif; font-size: 1.15rem; margin: 0; display: flex; align-items: center; gap: 0.5rem; }
        .wp-map-popover-cont { font-size: 0.82rem; color: var(--ink-soft); margin: 0.2rem 0 0; }

        .wp-map-search-results { background: #fff; border: 1px solid var(--hairline); border-top: none; border-radius: 0 0 10px 10px; margin-bottom: 1.4rem; overflow: hidden; }
        .wp-map-search-row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; padding: 0.8rem 1rem; border-top: 1px solid var(--hairline); }
        .wp-map-search-row:first-child { border-top: none; }
        .wp-map-search-row-info { cursor: pointer; flex: 1; min-width: 180px; }
        .wp-map-search-row-info:hover .wp-country-name { text-decoration: underline; }

        .wp-map-lists { display: grid; grid-template-columns: 1fr; gap: 1.6rem; margin-top: 1.6rem; }
        @media (min-width: 700px) { .wp-map-lists { grid-template-columns: 1fr 1fr; } }
        .wp-map-list-title { font-family: 'Fraunces', serif; font-size: 1.2rem; margin: 0 0 0.8rem; display: flex; align-items: center; gap: 0.5rem; }
        .wp-map-list-count { font-family: 'Work Sans', sans-serif; font-size: 0.8rem; font-weight: 600; color: var(--ink-soft); background: var(--parchment); border-radius: 999px; padding: 0.1rem 0.6rem; }
        .wp-map-list-empty { color: var(--ink-soft); font-size: 0.9rem; }
        .wp-map-list-group { margin-bottom: 1rem; }
        .wp-map-list-continent { font-size: 0.75rem; font-weight: 600; text-transform: none; color: var(--ink-soft); margin-bottom: 0.3rem; }
        .wp-map-list-row { display: flex; align-items: center; gap: 0.5rem; width: 100%; text-align: left; background: none; border: none; padding: 0.35rem 0; font-family: 'Work Sans', sans-serif; font-size: 0.92rem; color: var(--ink); cursor: pointer; }

        .wp-trips-page { max-width: 640px; }
        .wp-trip-card { display: block; width: 100%; text-align: left; background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.9rem 1.1rem; margin-bottom: 0.7rem; cursor: pointer; }
        .wp-trip-card:hover { border-color: var(--gold); }
        .wp-trip-card-top { display: flex; justify-content: space-between; align-items: center; gap: 0.6rem; }
        .wp-trip-card-name { font-family: 'Fraunces', serif; font-size: 1.02rem; display: flex; align-items: center; gap: 0.5rem; }
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
        .wp-trip-cost-value { font-family: 'Fraunces', serif; font-size: 1.2rem; margin: 0.1rem 0 0; }
        .wp-trip-stop-card { background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.8rem 1rem; margin-bottom: 0.4rem; }
        .wp-trip-stop-top { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.4rem; }
        .wp-trip-city-input { flex: 1; border: none; border-bottom: 1px solid var(--hairline); font-family: 'Fraunces', serif; font-size: 0.98rem; padding: 0.2rem 0; background: none; }
        .wp-trip-city-input:focus { outline: none; border-color: var(--gold); }
        .wp-trip-day-range { font-size: 0.75rem; color: var(--ink-soft); white-space: nowrap; }
        .wp-trip-remove-btn { background: none; border: none; color: var(--ink-soft); cursor: pointer; padding: 0.15rem; display: flex; flex-shrink: 0; }
        .wp-trip-remove-btn:hover { color: #B5453D; }
        .wp-trip-highlight-row { display: flex; align-items: center; gap: 0.5rem; padding: 0.35rem 0; border-top: 1px solid var(--hairline); }
        .wp-trip-highlight-text { flex: 1; font-size: 0.85rem; }
        .wp-trip-add-highlight-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.4rem; }
        .wp-trip-highlight-input { flex: 1 1 100px; min-width: 0; font-size: 0.85rem; padding: 0.4rem 0.6rem; border: 1px solid var(--hairline); border-radius: 8px; }
        .wp-trip-add-btn { background: var(--parchment); border: 1px solid var(--hairline); border-radius: 8px; padding: 0.4rem 0.6rem; cursor: pointer; display: flex; align-items: center; }
        .wp-trip-suggestions { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; }
        .wp-trip-suggestion-chip { display: flex; align-items: center; gap: 0.25rem; font-size: 0.76rem; background: var(--parchment); border: 1px solid var(--hairline); border-radius: 999px; padding: 0.25rem 0.6rem; cursor: pointer; color: var(--ink-soft); }
        .wp-trip-suggestion-chip:hover { border-color: var(--gold); color: var(--ink); }
        .wp-trip-transit-row { display: flex; flex-wrap: wrap; gap: 0.4rem; padding: 0.5rem 0.2rem; margin-left: 1rem; border-left: 2px dashed var(--hairline); }
        .wp-trip-transit-select, .wp-trip-transit-input { font-size: 0.78rem; padding: 0.35rem 0.5rem; border: 1px solid var(--hairline); border-radius: 8px; background: #fff; min-width: 0; }
        .wp-trip-transit-select { flex: 1 1 6rem; }
        .wp-trip-transit-input { flex: 1 1 5rem; min-width: 0; }
        .wp-trip-add-stop-btn { display: flex; align-items: center; justify-content: center; gap: 0.4rem; width: 100%; background: none; border: 1px dashed var(--hairline); border-radius: 10px; padding: 0.6rem; font-size: 0.85rem; color: var(--ink-soft); cursor: pointer; margin: 0.6rem 0 1.2rem; }
        .wp-trip-add-stop-btn:hover { border-color: var(--gold); color: var(--ink); }
        .wp-trip-footer-actions { display: flex; gap: 0.6rem; flex-wrap: wrap; }
        .wp-trip-delete-btn { background: none; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.55rem 1.1rem; font-size: 0.85rem; color: #B5453D; cursor: pointer; }
        .wp-trip-subsection { margin-top: 0.7rem; padding-top: 0.6rem; border-top: 1px solid var(--hairline); }
        .wp-trip-subsection-label { font-size: 0.72rem; color: var(--ink-soft); margin: 0 0 0.35rem; text-transform: uppercase; letter-spacing: 0.03em; }
        .wp-trip-typical-hint { font-size: 0.72rem; color: var(--ink-soft); margin: 0.2rem 0 0.6rem 1.2rem; }
        .wp-trip-export-btn { display: flex; align-items: center; gap: 0.4rem; background: none; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.5rem 1rem; font-size: 0.82rem; color: var(--ink); cursor: pointer; margin-bottom: 1.2rem; }
        .wp-trip-export-btn:hover { border-color: var(--gold); }
        .wp-trip-action-row { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1.2rem; }
        .wp-trip-action-row .wp-trip-export-btn { margin-bottom: 0; }
        .wp-trip-insert-before-btn { display: flex; align-items: center; gap: 0.3rem; width: 100%; background: none; border: none; font-size: 0.7rem; color: var(--ink-soft); cursor: pointer; padding: 0.25rem 0.4rem; opacity: 0.55; }
        .wp-trip-insert-before-btn:hover { opacity: 1; color: var(--gold); }
        .wp-trip-day-range-edit { display: flex; align-items: center; gap: 0.25rem; font-size: 0.75rem; color: var(--ink-soft); white-space: nowrap; }
        .wp-trip-day-num { width: 2.6rem; font-size: 0.75rem; padding: 0.2rem 0.3rem; border: 1px solid var(--hairline); border-radius: 6px; text-align: center; }
        .wp-trip-transit-num { flex: 0 0 3.4rem; text-align: center; }

        .wp-trip-daynote-row { padding: 0.4rem 0; border-top: 1px solid var(--hairline); }
        .wp-trip-daynote-label { font-size: 0.75rem; color: var(--ink-soft); display: block; margin-bottom: 0.3rem; }
        .wp-trip-daynote-input { width: 100%; font-family: 'Work Sans', sans-serif; font-size: 0.85rem; padding: 0.5rem 0.6rem; border: 1px solid var(--hairline); border-radius: 8px; resize: vertical; background: #fff; color: var(--ink); }
        .wp-trip-daynote-input:focus { outline: none; border-color: var(--gold); }
        .wp-trip-daynote-readonly { font-size: 0.85rem; color: var(--ink); margin: 0; white-space: pre-wrap; line-height: 1.5; }
        .wp-trip-city-readonly { flex: 1; font-family: 'Fraunces', serif; font-size: 0.98rem; }

        .wp-trip-share-box { background: #fff; border: 1px solid var(--hairline); border-radius: 12px; padding: 0.9rem 1.1rem; margin-bottom: 1.2rem; }
        .wp-trip-share-row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
        .wp-trip-share-title { font-family: 'Fraunces', serif; font-size: 0.95rem; margin: 0; }
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
        .wp-auth-title { font-family: 'Fraunces', serif; font-size: 1.4rem; font-weight: 600; margin: 0 0 0.4rem; }
        .wp-auth-subtitle { font-size: 0.86rem; color: var(--ink-soft); line-height: 1.45; margin: 0 0 1.3rem; }
        .wp-google-btn { display: flex; align-items: center; justify-content: center; gap: 0.6rem; width: 100%; background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.65rem 1rem; font-family: 'Work Sans', sans-serif; font-size: 0.9rem; font-weight: 600; color: var(--ink); cursor: pointer; }
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

        .wp-detail-tagline { font-family: 'Fraunces', serif; font-style: italic; font-weight: 500; font-size: 1.3rem; color: #463F30; margin: 0.5rem 0 1rem; max-width: 50ch; line-height: 1.45; }
        .wp-chip-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.3rem; }
        .wp-chip { background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.3rem 0.8rem; font-size: 0.8rem; color: var(--ink); }

        .wp-good-to-know { background: #fff; border: 1px solid var(--hairline); border-radius: 3px; padding: 1.1rem 1.2rem; margin-bottom: 1.9rem; }
        .wp-gtk-grid { display: grid; grid-template-columns: 1fr; gap: 1rem 1.4rem; margin-top: 0.7rem; }
        @media (min-width: 520px) { .wp-gtk-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (min-width: 760px) { .wp-gtk-grid { grid-template-columns: repeat(3, 1fr); } }
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
        .wp-faq-q { font-family: 'Fraunces', serif; font-weight: 600; font-size: 0.94rem; margin-bottom: 0.35rem; color: var(--ink); }
        .wp-faq-a { font-size: 0.86rem; line-height: 1.55; color: #4a4436; }

        .wp-pairs-wrap { margin-top: 2rem; }
        .wp-pairs-row { display: flex; flex-wrap: wrap; gap: 0.7rem; }
        .wp-pairs-card { display: flex; align-items: center; gap: 0.5rem; background: #fff; border: 1px solid var(--hairline); border-radius: 999px; padding: 0.5rem 0.9rem 0.5rem 0.7rem; cursor: pointer; font-family: 'Work Sans', sans-serif; font-size: 0.88rem; color: var(--ink); }
        .wp-pairs-card:hover { background: #FBF8F1; }

        .wp-footer { margin-top: 3.5rem; padding-top: 2rem; border-top: 1px solid var(--hairline); }
        .wp-footer-top { display: flex; flex-wrap: wrap; gap: 2.5rem; justify-content: space-between; margin-bottom: 1.6rem; }
        .wp-footer-brand { display: flex; gap: 0.65rem; max-width: 340px; }
        .wp-footer-brand-name { font-family: 'Fraunces', serif; font-size: 1.05rem; font-weight: 600; margin-bottom: 0.25rem; }
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
            {firebaseReady && !authLoading && (
              <button className={"wp-nav-link" + (view === "map" ? " wp-nav-link-active" : "")} onClick={() => goToStatic("map")}>{T.myMap}</button>
            )}
            {firebaseReady && !authLoading && (
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
        </nav>

        {view === "continents" && (
          <div className="wp-hero">
            <div className="wp-hero-text">
              <h1 className="wp-hero-headline">{T.heroHeadline}</h1>
              <p className="wp-tagline">{T.heroTagline}</p>
              <div className="wp-hero-stats">
                <div className="wp-hero-stat"><b>{allCountriesFlat.length}</b><span>{T.statsCountries}</span></div>
                <div className="wp-hero-stat"><b>{totalAttractions}+</b><span>{T.statsAttractions}</span></div>
                <div className="wp-hero-stat"><b>2</b><span>{T.statsLanguages}</span></div>
              </div>
              <div className="wp-hero-features">
                <button className="wp-hero-feature-card" onClick={() => document.querySelector(".wp-continent-grid") && document.querySelector(".wp-continent-grid").scrollIntoView({ behavior: "smooth" })}>
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

        {view === "continents" && (
          <div className="wp-search-wrap">
            <div className="wp-search-box">
              <Search size={16} className="wp-search-icon" />
              <input
                type="text"
                className="wp-search-input"
                placeholder={T.searchHome}
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
                    <Award size={26} style={{ color: "#B8863E" }} />
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
                    <Award size={30} style={{ color: "#B8863E" }} />
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

            <div className="wp-stat-grid">
              <StatBlock icon={Users} label={T.population} value={country.population} accent={continent.color} />
              <StatBlock icon={Languages} label={T.language} value={country.language} accent={continent.color} />
              <StatBlock icon={Coins} label={T.currency} value={country.currency} accent={continent.color} />
              <StatBlock icon={CalendarClock} label={T.bestTime} value={country.bestTime} accent={continent.color} />
            </div>

            <p className="wp-blurb">{country.blurb}</p>

            {(country.goodToKnow || country.budget || country.visa) && (
              <div className="wp-good-to-know">
                <h3 className="wp-section-title" style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}><ShieldCheck size={18} style={{ color: continent.color }} /> {T.tripEssentials}</h3>
                <div className="wp-gtk-grid">
                  {country.budget && <div><div className="wp-gtk-label">{T.dailyBudget}</div><div className="wp-gtk-value">{country.budget}</div></div>}
                  {country.visa && <div><div className="wp-gtk-label">{T.visa}</div><div className="wp-gtk-value">{country.visa}</div></div>}
                  {country.goodToKnow && <div><div className="wp-gtk-label">{T.plugVoltage}</div><div className="wp-gtk-value">{country.goodToKnow.plug}</div></div>}
                  {country.goodToKnow && <div><div className="wp-gtk-label">{T.tipping}</div><div className="wp-gtk-value">{country.goodToKnow.tipping}</div></div>}
                  {country.goodToKnow && <div><div className="wp-gtk-label">{T.safety}</div><div className="wp-gtk-value">{country.goodToKnow.safety}</div></div>}
                  {country.goodToKnow && <div><div className="wp-gtk-label">{T.gettingAround}</div><div className="wp-gtk-value">{country.goodToKnow.gettingAround}</div></div>}
                  {country.goodToKnow && country.goodToKnow.gettingThere && <div><div className="wp-gtk-label">{T.gettingThere}</div><div className="wp-gtk-value">{country.goodToKnow.gettingThere}</div></div>}
                </div>
              </div>
            )}

            {country.food && (
              <div style={{ marginBottom: "1.9rem" }}>
                <h3 className="wp-section-title" style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}><Utensils size={18} style={{ color: continent.color }} /> {T.tastesOf} {country.name}</h3>
                <div className="wp-food-grid">
                  {country.food.map((f, i) => (
                    <div className="wp-food-item" key={i}>
                      <div className="wp-food-name">{f.name}</div>
                      <div className="wp-food-desc">{f.desc}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            <h3 className="wp-section-title">{T.topAttractions}</h3>
            <div className="wp-attractions-grid">
              {country.attractions.map((a, i) => (
                <div key={i}>
                  <AttractionImage title={a.wiki} alt={a.name} />
                  <div className="wp-attraction-name">{a.name}</div>
                  <div className="wp-attraction-desc">{a.desc}</div>
                </div>
              ))}
            </div>

            <div className="wp-itinerary-wrap">
              <div className="wp-itinerary-head">
                <h3 className="wp-section-title" style={{ marginBottom: 0, display: "flex", alignItems: "center", gap: "0.5rem" }}><MapPinIcon size={18} style={{ color: continent.color }} /> {T.suggestedItinerary}</h3>
                <span className="wp-itinerary-total">{country.itineraryDays} {country.itineraryDays === 1 ? T.day : T.days}</span>
              </div>
              {country.daysReason && <p className="wp-days-reason">{country.daysReason}</p>}

              <CountryMap country={country} accentColor={continent.color} />

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

            {country.faq && country.faq.length > 0 && (
              <div className="wp-faq-wrap">
                <h3 className="wp-section-title" style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}><ShieldCheck size={18} style={{ color: continent.color }} /> {T.faqTitle}</h3>
                {country.faq.map((item, i) => (
                  <div className="wp-faq-item" key={i}>
                    <div className="wp-faq-q">{item.q}</div>
                    <div className="wp-faq-a">{item.a}</div>
                  </div>
                ))}
              </div>
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
                {visitedSparkline && (
                  <svg viewBox={"0 0 " + visitedSparkline.w + " " + visitedSparkline.h} className="wp-map-sparkline" preserveAspectRatio="none">
                    <path d={visitedSparkline.d} fill="none" stroke="#3F8F6F" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                )}
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
                            onClick={() => setCountryStatus(cty.id, "visited")}
                          >
                            <CheckCircle size={14} /> {T.markVisited}
                          </button>
                          <button
                            className={"wp-status-btn wp-status-want" + (countryStatuses[cty.id] === "want" ? " wp-status-active" : "")}
                            onClick={() => setCountryStatus(cty.id, "want")}
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

            <div
              className="wp-map-frame"
              onWheel={handleMapWheel}
              onPointerDown={handleMapPointerDown}
              onPointerMove={handleMapPointerMove}
              onPointerUp={handleMapPointerUp}
              onPointerLeave={handleMapPointerUp}
              style={{ cursor: mapZoom > 1 ? "grab" : "default", touchAction: "none" }}
            >
              <svg
                viewBox="0 0 2000 1001"
                className="wp-world-map"
                style={{ transform: "translate(" + mapPan.x + "px," + mapPan.y + "px) scale(" + mapZoom + ")", transition: mapDragRef.current.dragging ? "none" : "transform 0.18s ease-out" }}
              >
                {Object.keys(WORLD_MAP_BG_PATHS).map((iso) => {
                  const key = iso.toLowerCase();
                  const status = countryStatuses[key];
                  const cty = allCountriesForMap.find((c) => c.id === key);
                  return (
                    <path
                      key={"bg-" + iso}
                      d={WORLD_MAP_BG_PATHS[iso]}
                      className={status ? "wp-map-country wp-map-status-" + status : "wp-map-bg-country wp-map-clickable"}
                      onClick={() => handleMapCountryClick(cty)}
                    >
                      <title>{cty ? cty.name : iso}</title>
                    </path>
                  );
                })}
                {allCountriesFlat.filter((c) => WORLD_MAP_PATHS[c.id]).map((c) => (
                  <path
                    key={c.id}
                    d={WORLD_MAP_PATHS[c.id]}
                    className={"wp-map-country wp-map-status-" + (countryStatuses[c.id] || "none")}
                    onClick={() => handleMapCountryClick(c)}
                  >
                    <title>{c.name}</title>
                  </path>
                ))}
                {allCountriesFlat.filter((c) => WORLD_MAP_MARKERS[c.id]).map((c) => (
                  <circle
                    key={c.id}
                    cx={WORLD_MAP_MARKERS[c.id].x}
                    cy={WORLD_MAP_MARKERS[c.id].y}
                    r="9"
                    className={"wp-map-country wp-map-marker wp-map-status-" + (countryStatuses[c.id] || "none")}
                    onClick={() => handleMapCountryClick(c)}
                  >
                    <title>{c.name}</title>
                  </circle>
                ))}
                {Object.keys(WORLD_MAP_EXTRA_MARKERS).map((key) => {
                  const cty = allCountriesForMap.find((c) => c.id === key);
                  return (
                    <circle
                      key={"extra-" + key}
                      cx={WORLD_MAP_EXTRA_MARKERS[key].x}
                      cy={WORLD_MAP_EXTRA_MARKERS[key].y}
                      r="5"
                      className={"wp-map-country wp-map-marker wp-map-clickable wp-map-status-" + (countryStatuses[key] || "none")}
                      onClick={() => handleMapCountryClick(cty)}
                    >
                      <title>{cty ? cty.name : key}</title>
                    </circle>
                  );
                })}
              </svg>

              <div className="wp-map-zoom-controls">
                <button onClick={mapZoomIn} aria-label="Zoom in"><PlusIcon size={16} /></button>
                <button onClick={mapZoomOut} aria-label="Zoom out"><span style={{ fontSize: "18px", lineHeight: 1 }}>−</span></button>
                {mapZoom > 1 && <button onClick={mapZoomReset} className="wp-map-zoom-reset" aria-label="Reset zoom"><RefreshIcon size={14} /></button>}
              </div>
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

            {user && Object.values(trips).map((trip) => (
              <button
                key={trip.id}
                className="wp-trip-card"
                onClick={() => { setActiveTripId(trip.id); setView("trip-detail"); window.scrollTo(0, 0); }}
              >
                <div className="wp-trip-card-top">
                  <span className="wp-trip-card-name"><span>{trip.flag}</span>{trip.name}</span>
                  <span className={"wp-trip-status-badge" + (trip.status === "done" ? " wp-trip-status-done" : "")}>
                    {trip.status === "done" ? T.tripStatusDone : T.tripStatusPlanning}
                  </span>
                </div>
                <p className="wp-trip-card-meta">
                  {trip.startDate || "?"} – {trip.endDate || "?"} · {dayCount(trip.startDate, trip.endDate)} {T.days} · {trip.stops.length} {T.stops}
                </p>
              </button>
            ))}

            {user && (
              <button className="wp-quiz-btn wp-quiz-btn-primary" style={{ marginTop: "0.6rem" }} onClick={openNewTripForm}>
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
          const countryData = allCountriesFlat.find((c) => c.id === trip.countryId);
          const suggestions = countryData && countryData.attractions ? countryData.attractions.map((a) => a.name) : [];
          return (
            <div className="wp-trips-page">
              <button className="wp-trip-back" onClick={() => { setActiveTripId(null); goToStatic("trips"); }}>
                <ChevronRight size={15} style={{ transform: "rotate(180deg)" }} /> {T.myTrips}
              </button>

              <div className="wp-trip-detail-header">
                <div className="wp-trip-card-top">
                  <span className="wp-trip-card-name"><span>{trip.flag}</span>{trip.name}</span>
                  <span className={"wp-trip-status-badge" + (trip.status === "done" ? " wp-trip-status-done" : "")}>
                    {trip.status === "done" ? T.tripStatusDone : T.tripStatusPlanning}
                  </span>
                </div>
                <p className="wp-trip-card-meta">{trip.startDate || "?"} – {trip.endDate || "?"} · {total} {T.days} · {trip.stops.length} {T.stops}</p>
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

              <div className="wp-trip-action-row">
                <button className="wp-trip-export-btn" onClick={() => saveTripNow(trip.id)}>
                  <CheckCircle size={14} /> {tripSaveStatus === "saved" ? T.tripSaved : T.saveTrip}
                </button>
                <button className="wp-trip-export-btn" onClick={() => exportTripPDF(trip)}>
                  <Download size={14} /> {T.exportPdf}
                </button>
              </div>

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

              {trip.stops.map((stop, i) => (
                <div key={stop.id}>
                  <button className="wp-trip-insert-before-btn" onClick={() => insertStopBefore(trip.id, stop.id)}>
                    <PlusIcon size={11} /> {T.insertStopHere}
                  </button>
                  <div className="wp-trip-stop-card">
                    <div className="wp-trip-stop-top">
                      <input
                        type="text"
                        className="wp-trip-city-input"
                        placeholder={T.cityPlaceholder}
                        value={stop.city}
                        onChange={(e) => updateStopField(trip.id, stop.id, "city", e.target.value)}
                      />
                      <span className="wp-trip-day-range-edit">
                        {T.day}
                        <input type="number" min="1" className="wp-trip-day-num" value={stop.dayStart} onChange={(e) => updateStopField(trip.id, stop.id, "dayStart", parseInt(e.target.value) || 1)} />
                        -
                        <input type="number" min="1" className="wp-trip-day-num" value={stop.dayEnd} onChange={(e) => updateStopField(trip.id, stop.id, "dayEnd", parseInt(e.target.value) || 1)} />
                      </span>
                      {trip.stops.length > 1 && (
                        <button className="wp-trip-remove-btn" onClick={() => removeStop(trip.id, stop.id)} aria-label="Remove stop"><X size={14} /></button>
                      )}
                    </div>

                    {stop.highlights.map((h) => (
                      <div key={h.id} className="wp-trip-highlight-row">
                        <CheckCircle size={14} style={{ color: "#6B9E68", flexShrink: 0 }} />
                        <span className="wp-trip-highlight-text">{h.text}</span>
                        <button className="wp-trip-remove-btn" onClick={() => removeHighlight(trip.id, stop.id, h.id)} aria-label="Remove"><X size={12} /></button>
                      </div>
                    ))}

                    <div className="wp-trip-add-highlight-row">
                      <input
                        type="text"
                        className="wp-trip-highlight-input"
                        placeholder={T.addHighlightPlaceholder}
                        value={highlightDrafts[stop.id] || ""}
                        onChange={(e) => setHighlightDrafts({ ...highlightDrafts, [stop.id]: e.target.value })}
                        onKeyDown={(e) => {
                          if (e.key === "Enter" && (highlightDrafts[stop.id] || "").trim()) {
                            addHighlight(trip.id, stop.id, highlightDrafts[stop.id], "custom");
                            setHighlightDrafts({ ...highlightDrafts, [stop.id]: "" });
                          }
                        }}
                      />
                      <button
                        className="wp-trip-add-btn"
                        onClick={() => {
                          if ((highlightDrafts[stop.id] || "").trim()) {
                            addHighlight(trip.id, stop.id, highlightDrafts[stop.id], "custom");
                            setHighlightDrafts({ ...highlightDrafts, [stop.id]: "" });
                          }
                        }}
                      ><PlusIcon size={14} /></button>
                    </div>

                    {suggestions.length > 0 && (
                      <div className="wp-trip-suggestions">
                        {suggestions.filter((s) => !stop.highlights.some((h) => h.text === s)).slice(0, 4).map((s) => (
                          <button key={s} className="wp-trip-suggestion-chip" onClick={() => addHighlight(trip.id, stop.id, s, "attraction")}>
                            <PlusIcon size={11} /> {s}
                          </button>
                        ))}
                      </div>
                    )}

                    <div className="wp-trip-subsection">
                      <p className="wp-trip-subsection-label">{T.whereToSleep}</p>
                      {(stop.stays || []).map((st) => (
                        <div key={st.id} className="wp-trip-highlight-row">
                          <span style={{ fontSize: "0.85rem" }}>🏨</span>
                          <span className="wp-trip-highlight-text">{st.name}{st.nights ? " · " + st.nights + " " + T.nights : ""}{st.price ? " · " + st.price : ""}</span>
                          <button className="wp-trip-remove-btn" onClick={() => removeStay(trip.id, stop.id, st.id)} aria-label="Remove"><X size={12} /></button>
                        </div>
                      ))}
                      <div className="wp-trip-add-highlight-row">
                        <input type="text" className="wp-trip-highlight-input" style={{ flex: 2 }} placeholder={T.stayNamePlaceholder}
                          value={(stayDrafts[stop.id] || {}).name || ""}
                          onChange={(e) => setStayDrafts({ ...stayDrafts, [stop.id]: { ...(stayDrafts[stop.id] || {}), name: e.target.value } })} />
                        <input type="text" className="wp-trip-highlight-input" style={{ flex: 1 }} placeholder={T.nightsPlaceholder}
                          value={(stayDrafts[stop.id] || {}).nights || ""}
                          onChange={(e) => setStayDrafts({ ...stayDrafts, [stop.id]: { ...(stayDrafts[stop.id] || {}), nights: e.target.value } })} />
                        <input type="text" className="wp-trip-highlight-input" style={{ flex: 1 }} placeholder={T.transitPrice}
                          value={(stayDrafts[stop.id] || {}).price || ""}
                          onChange={(e) => setStayDrafts({ ...stayDrafts, [stop.id]: { ...(stayDrafts[stop.id] || {}), price: e.target.value } })} />
                        <button className="wp-trip-add-btn" onClick={() => {
                          const d = stayDrafts[stop.id] || {};
                          addStay(trip.id, stop.id, d.name || "", d.nights || "", d.price || "");
                          setStayDrafts({ ...stayDrafts, [stop.id]: {} });
                        }}><PlusIcon size={14} /></button>
                      </div>
                    </div>

                    <div className="wp-trip-subsection">
                      <p className="wp-trip-subsection-label">{T.whereToEat}</p>
                      {(stop.meals || []).map((m) => (
                        <div key={m.id} className="wp-trip-highlight-row">
                          <span style={{ fontSize: "0.85rem" }}>🍽</span>
                          <span className="wp-trip-highlight-text">{m.name}</span>
                          <button className="wp-trip-remove-btn" onClick={() => removeMeal(trip.id, stop.id, m.id)} aria-label="Remove"><X size={12} /></button>
                        </div>
                      ))}
                      <div className="wp-trip-add-highlight-row">
                        <input type="text" className="wp-trip-highlight-input" placeholder={T.addMealPlaceholder}
                          value={(mealDrafts[stop.id] || {}).name || ""}
                          onChange={(e) => setMealDrafts({ ...mealDrafts, [stop.id]: { ...(mealDrafts[stop.id] || {}), name: e.target.value } })}
                          onKeyDown={(e) => {
                            if (e.key === "Enter" && ((mealDrafts[stop.id] || {}).name || "").trim()) {
                              addMeal(trip.id, stop.id, mealDrafts[stop.id].name);
                              setMealDrafts({ ...mealDrafts, [stop.id]: {} });
                            }
                          }} />
                        <button className="wp-trip-add-btn" onClick={() => {
                          const d = mealDrafts[stop.id] || {};
                          addMeal(trip.id, stop.id, d.name || "");
                          setMealDrafts({ ...mealDrafts, [stop.id]: {} });
                        }}><PlusIcon size={14} /></button>
                      </div>
                      {countryData && countryData.food && countryData.food.length > 0 && (
                        <div className="wp-trip-suggestions">
                          {countryData.food.filter((f) => !stop.meals.some((m) => m.name === f.name)).slice(0, 3).map((f) => (
                            <button key={f.name} className="wp-trip-suggestion-chip" onClick={() => addMeal(trip.id, stop.id, f.name)}>
                              <PlusIcon size={11} /> {f.name}
                            </button>
                          ))}
                        </div>
                      )}
                    </div>

                    <div className="wp-trip-subsection">
                      <p className="wp-trip-subsection-label">{T.dayNotes}</p>
                      {Array.from({ length: Math.max(1, stop.dayEnd - stop.dayStart + 1) }, (_, di) => stop.dayStart + di).map((day) => (
                        <div key={day} className="wp-trip-daynote-row">
                          <span className="wp-trip-daynote-label">{T.day} {day}</span>
                          <textarea
                            className="wp-trip-daynote-input"
                            placeholder={T.dayNotesPlaceholder}
                            rows={2}
                            value={(trip.dailyNotes || {})[day] || ""}
                            onChange={(e) => updateDailyNote(trip.id, day, e.target.value)}
                          />
                        </div>
                      ))}
                    </div>
                  </div>

                  {i < trip.stops.length - 1 && trip.transits.find((tr) => tr.afterStopId === stop.id) && (
                    <div className="wp-trip-transit-row">
                      <select
                        className="wp-trip-transit-select"
                        value={trip.transits.find((tr) => tr.afterStopId === stop.id).mode}
                        onChange={(e) => updateTransit(trip.id, stop.id, "mode", e.target.value)}
                      >
                        <option value="">{T.chooseTransit}</option>
                        <option value="flight">{T.transitFlight}</option>
                        <option value="train">{T.transitTrain}</option>
                        <option value="bus">{T.transitBus}</option>
                        <option value="car">{T.transitCar}</option>
                        <option value="boat">{T.transitBoat}</option>
                      </select>
                      <input
                        type="number"
                        min="0"
                        className="wp-trip-transit-input wp-trip-transit-num"
                        placeholder={T.hoursLabel}
                        value={trip.transits.find((tr) => tr.afterStopId === stop.id).durationHours}
                        onChange={(e) => updateTransit(trip.id, stop.id, "durationHours", e.target.value)}
                      />
                      <input
                        type="number"
                        min="0"
                        max="59"
                        className="wp-trip-transit-input wp-trip-transit-num"
                        placeholder={T.minutesLabel}
                        value={trip.transits.find((tr) => tr.afterStopId === stop.id).durationMinutes}
                        onChange={(e) => updateTransit(trip.id, stop.id, "durationMinutes", e.target.value)}
                      />
                      <input
                        type="text"
                        className="wp-trip-transit-input"
                        placeholder={T.transitPrice}
                        value={trip.transits.find((tr) => tr.afterStopId === stop.id).price}
                        onChange={(e) => updateTransit(trip.id, stop.id, "price", e.target.value)}
                      />
                    </div>
                  )}
                  {i < trip.stops.length - 1 && trip.transits.find((tr) => tr.afterStopId === stop.id) && trip.transits.find((tr) => tr.afterStopId === stop.id).mode && (
                    <p className="wp-trip-typical-hint">{T.typicalRange}: {TRANSIT_TYPICAL[trip.transits.find((tr) => tr.afterStopId === stop.id).mode]}</p>
                  )}
                </div>
              ))}

              <button className="wp-trip-add-stop-btn" onClick={() => addStop(trip.id)}>
                <PlusIcon size={15} /> {T.addStop}
              </button>

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
                    const dayNums = Array.from({ length: Math.max(1, stop.dayEnd - stop.dayStart + 1) }, (_, di) => stop.dayStart + di);
                    const notedDays = dayNums.filter((day) => (notes[day] || "").trim());
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

                          {notedDays.length > 0 && (
                            <div className="wp-trip-subsection">
                              <p className="wp-trip-subsection-label">{T.dayNotes}</p>
                              {notedDays.map((day) => (
                                <div key={day} className="wp-trip-daynote-row">
                                  <span className="wp-trip-daynote-label">{T.day} {day}</span>
                                  <p className="wp-trip-daynote-readonly">{notes[day]}</p>
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
              <div style={{ fontFamily: "'Fraunces', serif", fontSize: "1.25rem", fontWeight: 600, marginBottom: "0.5rem" }}>Ten Days of Silence: A Solo Self-Drive Through Namibia</div>
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
              <div style={{ fontFamily: "'Fraunces', serif", fontSize: "1.3rem", fontWeight: 600, marginBottom: "0.6rem" }}>Namibia Self-Drive Checklist &amp; Planner</div>
              <p style={{ fontSize: "0.95rem", color: "#4a4436", lineHeight: 1.6, marginBottom: "1.1rem" }}>The route at a glance, what to book months ahead, offline driving apps that actually work, and a gear checklist — everything from the Namibia trip report, organized into a printable planner.</p>
              <button
                onClick={() => goToStatic("newsletter")}
                style={{ display: "inline-block", background: "var(--navy)", color: "#F6F2E8", border: "none", cursor: "pointer", padding: "0.7rem 1.4rem", borderRadius: "999px", fontSize: "0.9rem", fontWeight: 600, fontFamily: "'Work Sans', sans-serif" }}
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
