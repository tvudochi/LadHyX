#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define Path_Base_Dat "/home/toai/Developpement/LadHyX/LadHyX/publications/Data/base-search.dat"
#define Get_Var_Env "QUERY_STRING"

typedef struct Base_Data {
 char *Annee;
 char *Infos;
 struct Base_Data *suite;
} TBaseDat;

int Compteur=0;

/*---------------------------------- TsIncl -----------------------------------*/
/* test si la chaine t est dans la chaine s avec '|' ou ' ' comme separateur   */

char TsIncl(char *s, char *t) {
char i=0;

if ( ! t ) return 5;
while (*s != '\0') {
 i=0; while (t[i] && *s == t[i]) { s++; i++; }
 if ( (t[i] == '\0') && ((*s == ' ') || (*s == '\0')) )  return 1;
 s++; }
return 0;
}
/*---------------------------------- TrCar -----------------------------------*/
/* retourne un pointeur un caractere apres le niem '\0' de la chaine s        */

char *TrCar(char *s, char n) {

while ( n ) if (*s++ == '\0') n--;
return s;
}

/*------------------------------ LitEnv ----------------------------------*/
char *LitEnv () {

char *p=NULL, n;

if ( getenv(Get_Var_Env) ) {
  n = strlen(getenv(Get_Var_Env));
  p = (char *) malloc (n+2);
  p = getenv(Get_Var_Env);
  p[n] = '&'; p[n+1] = '\0';
  }
return p;
}

/*----------------------------- LitStdin ---------------------------------*/
char *LitStdin (char *Arg1) {

char *p=NULL, n;

if ( Arg1 ) {
  n = strlen(Arg1);
  p = (char *) malloc (n+2);
  p = Arg1;
  p[n] = '&'; p[n+1] = '\0';
  }
return p;
}

/*--------------------------------- LitVar -----------------------------------*/
char *LitVar(char *chaine, const char *nom) {

char *p, *u=NULL, n=strlen(nom);

if ( p = (char *)strstr(chaine,nom) ) {
  p += n + 1;
  if ( n = (char *)strchr(p,'&') - p ) {
    u = (char *) malloc (n + 1);
    strncpy(u,p,n); u[n]='\0';
    } }
return u;
}
/*---------------------------------- CrCpCh ----------------------------------*/
/* Creation et copy de chaine avec calcul de longeur (\0 compris)             */
char *CrCpCh(char *t) {
char *s;
int n;

n = strlen(t) + 1;
s  = (char *) malloc (n);
while (*s++ = *t++) ; s -= n; 
return s;
}
/*--------------------------------- liltf ------------------------------------*/
/* copy la ligne courante de f dans s substitue | en \0 et puis               */
/* retourne 1 si la ligne comporte n '|'                                      */
char liltf(char *s, int n, FILE *f) {
int c;

while ( (c = fgetc(f)) != EOF && c != '\n' ) 
  if  ((*s++ = c) == '|') { s--; *s++ = '\0'; n--; } 
*s = '\0';
return ( n != 0) ? 0 : 1;
}
/*------------------------------ CrbaseDat -----------------------------------*/
/* Lecture des lignes conportant 5 '|' dans le fichier Path_Base_Dat, puis   */
/* chainages des info avec comptabilisation des elets trouvés en f(Vd,Va,Ve). */

TBaseDat *CrbaseDat(char *Vd, char *Va, char *Ve) {
char Li[960];
FILE *f;
TBaseDat *p,*u;
int t=sizeof(TBaseDat);

p = (TBaseDat *) malloc(t); p->suite = NULL; u = p;
f = fopen(Path_Base_Dat,"r");
while ( liltf(Li,5,f) ) { 
   if ( TsIncl(Li,Vd) && TsIncl(TrCar(Li,1),Va) && TsIncl(TrCar(Li,2),Ve) ) { 
     u = u->suite = (TBaseDat *) malloc(t);
     u->Annee = CrCpCh(Li);
     u->Infos = CrCpCh(TrCar(Li,4));
     u->suite=NULL;
     Compteur++;} }
fclose(f);
u=p; p=p->suite; free(u);
return p;
}

/*----------------------------------------------------------------------------*/
void affch(char *p, const char *m) {

if (p) printf("\n%s : %s",m,p); else printf("\n%s : %d",m,p);
}
/*----------------------------------------------------------------------------*/
void afelt (TBaseDat *p) {
printf("\nBase->Annee : %s",p->Annee);
printf("\nBase->Infos : %s",p->Infos);
printf("\nBase->suite : %d\n",p->suite);
}
/*----------------------------------------------------------------------------*/
void En_Tete () {


printf("<!doctype html>\n<!--[if lte IE 7]> <html class=\"no-js ie67 ie678\" lang=\"en\"> <![endif]-->\n");
printf("<!--[if IE 8]> <html class=\"no-js ie8 ie678\" lang=\"en\"> <![endif]-->\n");
printf("<!--[if IE 9]> <html class=\"no-js ie9\" lang=\"en\"> <![endif]-->\n");
printf("<!--[if gt IE 9]> <!-->\n");
printf("<html class=\"no-js\" lang=\"en\">\n");
printf("<!--<![endif]-->\n");
printf("<head><meta charset=\"ISO-8859-1\">\n<!--[if IE]><meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"><![endif]-->\n");
printf("<title>LadHyX</title>\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<!--[if lt IE 9]>\n");
printf("<script src=\"trunk/html5.js\"></script>\n<![endif]-->\n<meta name=\"description\" content=\"Laboratoire Hydrodynamique LadHyX ladhyx \"/>\n");


printf("<link rel=\"stylesheet\" href=\"/Django-pub/css/knacss-unminified.css\" media=\"all\">\n<link rel=\"stylesheet\" href=\"/Django-pub/css/publications.css\" media=\"all\">\n</head>\n");
printf("<body>\n<div class=\"row\"><div class=\"col txtcenter\"><h4 id=\"titre\">Refereed Publications</h4></div></div>\n");
printf("<div class=\"row\">");

if ( Compteur > 5 ) {
  printf("<div class=\"col txtcenter\"><h4 id=\"titre\">Search Result(s) : %d</h4></div></div>\n",Compteur);
  printf("<div class=\"row\" id=\"index\">\n<div class=\"\" id=\"blank\"></div>\n");
  printf("<div class=\"col txtcenter w10\"><a href=\"/Django-pub/publi.rp_en.html\">Index</a></div>\n");
  printf("<div id=\"blank\"></div></div><br>\n\n");
  }
else
  printf("<div class=\"col txtcenter\"><h4 id=\"titre\">Search Result(s) : %d</h4></div></div>\n\n",Compteur);

}
/*------------------------------------
Lecture sur StdIn de 3 arguments Annee Auteur Journal
si 0 --> tous les annees ou tous les auteurs..etc

Les codes des valeurs pour les Auteurs et les journaux 
sont dans ../Data/info-publi.dat
Awxxxx 	--> pour les auteurs
Edxx	--> pour les journaux

ex :	./search-pub-rp-stdin.exe 0 Auamandolese Ed29
	./search-pub-rp-stdin.exe 0 Auamandolese 0
-------------------------------------*/

main (int argc, char *argv[]) {

char *p, *AnneeR=NULL, *AutrP=NULL, *EditC=NULL;
int n=1;
TBaseDat *BaseDat,*ptmp;


if ( argc == 4) {
  
  /* p     = LitEnv();
  p     = LitStdin(argv[1]);
  AutrP = LitVar(p,"AutrP");
  EditC = LitVar(p,"EditC");
  DomRe = LitVar(p,"DomRe");
  */
  
  if(strcmp(argv[1],"0")!=0) AnneeR = argv[1];
  if(strcmp(argv[2],"0")!=0) AutrP  = argv[2];
  if(strcmp(argv[3],"0")!=0) EditC  = argv[3];
  
  
  /*printf("Content-type: text/html\n\n");*/
  /*affch(p,"Env"); affch(AutrP,"AutrP"); affch(EditC,"EditC"); affch(DomRe,"DomRe");*/
  
  BaseDat = CrbaseDat(AnneeR,AutrP,EditC);
  ptmp    = BaseDat;
  
  /* En_Tete(); */
  
  while ( ptmp ) {
    /* printf("%s\n",ptmp->Infos);*/
    printf("%s+%s\n",ptmp->Annee,ptmp->Infos);
    ptmp = ptmp->suite; }
  } 
else {
  printf("\n** Lecture sur StdIn de 3 arguments Annee Auteur Journal.\n");
  printf("\n** Si 0 --> tous les annees ou tous les auteurs..etc.\n\n");

  printf("** Les codes des valeurs pour les Auteurs et les journaux sont dans ../Data/info-publi.dat\n");
  printf("**    Awxxxx 	--> pour les auteurs\n");
  printf("**    Edxx	--> pour les journaux\n\n");
  
  printf("** ex :	./search-pub-rp-stdin.exe 0 Auamandolese Ed29\n");
  printf("** ex :	./search-pub-rp-stdin.exe 0 Auamandolese 0\n\n");

}

}

