from django.views.generic import TemplateView
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    # Energie et transport
    url(r'^systeme-eoliens-et-hydroliens$',
        TemplateView.as_view(template_name="systeme-eoliens-et-hydroliens.html"),
        name="systeme-eoliens-et-hydroliens"),
    url(r'^ingenierie-du-vent-et-vibrations$',
        TemplateView.as_view(template_name="ingenierie-du-vent-et-vibrations.html"),
        name="ingenierie-du-vent-et-vibrations"),
    url(r'^aerodynamique-et-performance$',
        TemplateView.as_view(template_name="aerodynamique-et-performance.html"),
        name="aerodynamique-et-performance"),
    url(r'^transport-sans-contact$',
        TemplateView.as_view(template_name="transport-sans-contact.html"),
        name="transport-sans-contact"),
    url(r'^locomotion$',
        TemplateView.as_view(template_name="locomotion.html"),
        name="locomotion"),
    url(r'^transport-ecoulement-micro$',
        TemplateView.as_view(template_name="transport-ecoulement-micro.html"),
        name="transport-ecoulement-micro"),
    # Environnement

    url(r'^ecoulements-geophysiques$',
        TemplateView.as_view(template_name="ecoulements-geophysiques.html"),
        name="ecoulements-geophysiques"),
    url(r'^dispersion-des-polluants$',
        TemplateView.as_view(template_name="dispersion-des-polluants.html"),
        name="dispersion-des-polluants"),
    url(r'^dissipation-energetique$',
        TemplateView.as_view(template_name="dissipation-energetique.html"),
        name="dissipation-energetique"),
    url(r'^melange-des-oceans$',
        TemplateView.as_view(template_name="melange-des-oceans.html"),
        name="melange-des-oceans"),
    url(r'^recuperation-eau-douce$',
        TemplateView.as_view(template_name="recuperation-eau-douce.html"),
        name="recuperation-eau-douce"),
    url(r'^wind-waves$',
        TemplateView.as_view(template_name="wind-waves.html"),
        name="wind-waves"),
    # Design et société

    # #################################Art et science
    url(r'^art-et-science$',
        TemplateView.as_view(template_name="art-et-science.html"),
        name="art-et-science"),

    url(r'^art-et-science/approche-philosophique-et-epistemologique$',
        TemplateView.as_view(template_name="approche-philosophique-et-epistemologique.html"),
        name="approche-philosophique-et-epistemologique"),

    url(r'^art-et-science/art-science-innovation-et-entreprenariat-culturelle$',
        TemplateView.as_view(
            template_name="art-science-innovation-et-entreprenariat-culturelle.html"),
        name="art-science-innovation-et-entreprenariat-culturelle"),

    url(r'^art-et-science/mist-collector$',
        TemplateView.as_view(template_name="mist-collector.html"),
        name="mist-collector"),

    url(r'^art-et-science/transmutation-de-base$',
        TemplateView.as_view(template_name="transmutation-de-base.html"),
        name="transmutation-de-base"),

    url(r'^art-et-science/luminous-drift-climat-de-saturne$',
        TemplateView.as_view(template_name="luminous-drift-climat-de-saturne.html"),
        name="luminous-drift-climat-de-saturne"),

    url(r'^art-et-science/arc-avec-ensa-de-dijon$',
        TemplateView.as_view(template_name="arc-avec-ensa-de-dijon.html"),
        name="arc-avec-ensa-de-dijon"),

    url(r'^art-et-science/redshift-voyage-temporel-et-mythe-de-pan$',
        TemplateView.as_view(template_name="redshift-voyage-temporel-et-mythe-de-pan.html"),
        name="redshift-voyage-temporel-et-mythe-de-pan"),

    url(r'^art-et-science/redshift-n020-malevitch-dialogue-avec-takis$',
        TemplateView.as_view(template_name="redshift-n020-malevitch-dialogue-avec-takis.html"),
        name="redshift-n020-malevitch-dialogue-avec-takis"),

    url(r'^art-et-science/wave$',
        TemplateView.as_view(template_name="wave.html"),
        name="wave"),

    url(r'^art-et-science/exoplanet-un-cosmos-habite-de-plancton-bioluminescent$',
        TemplateView.as_view(template_name="exoplanet-un-cosmos-habite-de-plancton-bioluminescent.html"),
        name="exoplanet-un-cosmos-habite-de-plancton-bioluminescent"),

    url(r'^art-et-science/2080-performance-et-installation-sur-loxygene-de-lair$',
        TemplateView.as_view(template_name="2080-performance-et-installation-sur-loxygene-de-lair.html"),
        name="2080-performance-et-installation-sur-loxygene-de-lair"),

    url(r'^art-et-science/fluxus$',
        TemplateView.as_view(template_name="fluxus.html"),
        name="fluxus"),

    url(r'^art-et-science/infini-jeu-deau-avec-luniversite-du-havre$',
        TemplateView.as_view(template_name="infini-jeu-deau-avec-luniversite-du-havre.html"),
        name="infini-jeu-deau-avec-luniversite-du-havre"),

    # ############################# END ART ET SCIENCE

    url(r'^fabrication-du-verre$',
        TemplateView.as_view(template_name="fabrication-du-verre.html"),
        name="fabrication-du-verre"),
    url(r'^nouveaux-materiaux$',
        TemplateView.as_view(template_name="nouveaux-materiaux.html"),
        name="nouveaux-materiaux"),
    url(r'^textiles-intelligents$',
        TemplateView.as_view(template_name="textiles-intelligents.html"),
        name="textiles-intelligents"),

    # Physique du Sport
    url(r'^physique-du-sport$',
        TemplateView.as_view(template_name="physique-du-sport.html"),
        name="physique-du-sport"),
    url(r'^physique-du-sport/sport-mouvement-et-sante$',
        TemplateView.as_view(template_name="sport-mouvement-et-sante.html"),
        name="sport-mouvement-et-sante"),
    url(r'^physique-du-sport/sport-de-glisse-et-transport-a-faible-cout$',
        TemplateView.as_view(template_name="sport-de-glisse-et-transport-a-faible-cout.html"),
        name="sport-de-glisse-et-transport-a-faible-cout"),
    url(r'^physique-du-sport/sport-et-materiaux-pour-la-performance$',
        TemplateView.as_view(template_name="sport-et-materiaux-pour-la-performance.html"),
        name="sport-et-materiaux-pour-la-performance"),
    url(r'^physique-du-sport/videos-et-conferences$',
        TemplateView.as_view(template_name="videos-et-conferences.html"),
        name="videos-et-conferences"),
    # END physique du Sport

    # Econophysics
    url(r'^econophysics$',
        TemplateView.as_view(template_name="econophysics.html"),
        name="econophysics"),

    # Biomecanique et santé
    url(r'^diagnostique-cellulaire$',
        TemplateView.as_view(template_name="diagnostique-cellulaire.html"),
        name="diagnostique-cellulaire"),
    url(r'^biomecanique-et-biomimetique-vegetale$',
        TemplateView.as_view(template_name="biomecanique-et-biomimetique-vegetale.html"),
        name="biomecanique-et-biomimetique-vegetale"),
    url(r'^biomecanique-cellulaire$',
        TemplateView.as_view(template_name="biomecanique-cellulaire.html"),
        name="biomecanique-cellulaire"),
    # Biomecanique cardiovasculaire
    url(r'^biomecanique-cardiovasculaire$',
        TemplateView.as_view(template_name="biomecanique-cardiovasculaire.html"),
        name="biomecanique-cardiovasculaire"),

    url(r'^biomecanique-cardiovasculaire/what-should-tomorrow-drug-eluting-stent-look-like$',
        TemplateView.as_view(template_name="what-should-tomorrow-drug-eluting-stent-look-like.html"),
        name="what-should-tomorrow-drug-eluting-stent-look-like"),

    url(r'^biomecanique-cardiovasculaire/how-to-avoid-stent-complications$',
        TemplateView.as_view(template_name="how-to-avoid-stent-complications.html"),
        name="how-to-avoid-stent-complications"),

    url(r'^biomecanique-cardiovasculaire/how-do-cells-respond-to-mechanical-stimulation$',
        TemplateView.as_view(template_name="how-do-cells-respond-to-mechanical-stimulation.html"),
        name="how-do-cells-respond-to-mechanical-stimulation"),

    url(r'^biomecanique-cardiovasculaire/cellular-internalization-of-nanoparticles$',
        TemplateView.as_view(template_name="cellular-internalization-of-nanoparticles.html"),
        name="cellular-internalization-of-nanoparticles"),

    url(r'^biomecanique-cardiovasculaire/what-is-the-impact-of-cell-shape-on-vascular-cell-mechanotransduction$',
        TemplateView.as_view(template_name="what-is-the-impact-of-cell-shape-on-vascular-cell-mechanotransduction.html"),
        name="what-is-the-impact-of-cell-shape-on-vascular-cell-mechanotransduction"),

    url(r'^biomecanique-cardiovasculaire/what-are-the-effects-of-stent-degradation-on-the-arterial-wall$',
        TemplateView.as_view(template_name="what-are-the-effects-of-stent-degradation-on-the-arterial-wall.html"),
        name="what-are-the-effects-of-stent-degradation-on-the-arterial-wall"),

]
