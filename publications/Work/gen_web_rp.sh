#!/bin/sh

#-------------------------------------------------------------------------------
# Ce script utilise le fichier de données $PathData/$PubliBase pour generer deux
# bases reduites dans $PathData/$Basemodif et $PathData/$BaseSearch.
#
# Ces bases sont utilisees par le CMS Django et un programme de recherche
# search-pub.exe (langage C) pour la recherche par auteurs et/ou revues.
#
#
#------------------------------- INITIALISATION --------------------------------
#-------------------------------------------------------------------------------
#
# Var inter fonction

Err=0; VarTmp=""; BaseDat=""; MisFor=""

# Var champs de Base
AutrL=""; Titre=""; EditC=""; Statu=""; Annee=""; Volum=""
PageD=""; PageF=""; Abstr=""; PrPri=""; Ident=""; DomRS=""; MotCl=""


# Chemins et Fichiers
WorkDir="/srv/www/Django-publications/Scripts"
PathData="/srv/www/Django-publications/Data"
PathWeb="/DataWeb/html"
RelPath="/Django-pub"


InfoPubli="info-publi.dat"
PubliBase="base_publi.rp.dat"
TarDoc="docs.tgz"
TraceModif="tracemodif.dat"
Basemodif="publi.rp.dat"
BaseSearch="base-search.dat"


#-----------------------------------------------------------------------------------------------------------------------
#18/12/14-------------------------- LitPubli -----------------------------------
#-------------------------------------------------------------------------------
# Export dans l'environnement les variables associées a la pub $1 (ident)
#
LitPubli () {

VarTmp=`echo "$BaseDat" | grep -F "|$1|" | awk -F '|' '{print "Annee=\"" $1 "\"; EditC=\"" $2 "\"; Titre=\"" $4 \
	"\"; AutrL=\"" $5  "\"; Statu=\"" $6  "\"; Volum=\"" $7 "\"; PageD=\"" $8 "\"; PageF=\"" $9  		\
	"\"; Abstr=\"" $10 "\"; PrPri=\"" $11 "\"; DomRS=\"" $12 "\"; MotCl=\"" $13 "\"" }'`
eval "$VarTmp"
}

#-----------------------------------------------------------------------------------------------------------------------
#18/12/14------------------------ Extension ------------------------------------
#-------------------------------------------------------------------------------
# Retourne l'extension associée a $1 
Extension () {
tmp="${1#???}"
case $tmp in
"d") VarTmp="pdf";;
"s") VarTmp="ps";;
"g") VarTmp="ps.gz";;
"r") VarTmp="url";;
  *) VarTmp="html";;
esac
}

#-----------------------------------------------------------------------------------------------------------------------
#24/04/17----------------------- GenererBaseSearch -----------------------------
#-------------------------------------------------------------------------------
# utilisation de $PubliBase, info-publi.dat
# ==> creation de $BaseSearch

GenererBaseSearch () {

# tri : alphabétique sur le champ 3 et -r reverse, -n numerique sur le champ 1
BaseDat=`cat $PathData/$PubliBase | sort -t\| -k1nr -k3`
# Liste des Ident
LISTE=`echo "$BaseDat" | awk -F'|' '{print $3}'`
# Liste des auteurs lue dans $PathData/$InfoPubli (on garde les champs clef et initiales. nom) 
ListeA=`grep -E "^Au.*\|" $PathData/$InfoPubli | sed -e "s/ /\&nbsp;/g" | awk -F'|' '{print $1 "|" $3}'`
# Liste des Revues
ListeR=`grep -E "^Ed.*\|" $PathData/$InfoPubli | sed -e "s/ /\&nbsp;/g"`

# Pour chaque ident de la base, on fait la mise en forme (MeF) des données
for j in $LISTE; do
  LitPubli $j
  MisFor=""

  # MeF Editeur
  EditI=`echo "$ListeR" | grep -E "^$EditC\|" | awk -F'|' '{print $2}'`;

  # Mef Liste des auteurs
  aux=""; tmp1=""
  for k in $AutrL; do
    tmp1="$tmp1, $aux"
    aux=`echo "$ListeA" | grep -E "^$k\|" | awk -F'|' '{print $2}'`;
  done
  if [ "$tmp1" = ", " ]; then tmp1="$aux."; else tmp1="${tmp1#, , } and $aux."; fi
  ## MisFor="$MisFor<p id=\"Marges\">$tmp1 $Titre.<EM> " 
  MisFor="$tmp1+$Titre" 

  # MeF Statut et references
  case $Statu in
	"Stsub") MisFor="$MisFor+Submitted to $EditI+";;
	"Stinp") MisFor="$MisFor+$EditI, In press.+";;
	"Stacc") MisFor="$MisFor+Accepted in $EditI+";;
          *) if [ "$PageD" = "0" ] && [ "$PageF" = "0" ]; then
		MisFor="$MisFor+$EditI+$Volum"
	     else
	     	MisFor="$MisFor+$EditI+$Volum:$PageD-$PageF"
	     fi ;;
  esac
  Abs=""; Prp="";

  # MeF Abstract
  if [ "$Abstr" != "Rsno" ]; then Extension "$Abstr"; FileDoc=$j"ab.$VarTmp"
    if [ -e $PathWeb$RelPath/documents/$FileDoc ]; then Abs="$FileDoc"; fi
  fi
  
  # MeF Pre-Print
  if [ "$PrPri" != "Ppno" ]; then Extension "$PrPri"; FileDoc=$j"pp.$VarTmp"
    if [ -e $PathWeb$RelPath/documents/$FileDoc ]; then Prp="$FileDoc"; fi
    fi
  MisFor="$MisFor+$Abs+$Prp"

  # MeF ajout de la nouvelle ligne au fichier BaseSearch
  echo "$Annee|$AutrL|$EditC|$DomRS|$MisFor|" >> $BaseSearch    
done

# deplacement de BaseSearch dans Data
\mv -f $WorkDir/$BaseSearch $PathData/$BaseSearch
}

#-----------------------------------------------------------------------------------------------------------------------
#20/04/17------------------------- GenererBasemodif ----------------------------
#-------------------------------------------------------------------------------
# utilisation de $PubliBase, info-publi.dat
# creation de Basemodif (publi.rp.dat)
# Lecture dans info-publi.dat et substitution des elements auteurs et noms des
# journaux....

GenererBasemodif () {

# tri : alphabétique sur le champ 3 et -r reverse, -n numerique sur le champ 1
BaseDat=`cat $PathData/$PubliBase | sort -t\| -k1nr -k3`
# Liste des Ident
LISTE=`echo "$BaseDat" | awk -F'|' '{print $3}'`
# Liste des auteurs lue dans $PathData/$InfoPubli (on garde les champs clef et initiales. nom) 
ListeA=`grep -E "^Au.*\|" $PathData/$InfoPubli | sed -e "s/ /\&nbsp;/g" | awk -F'|' '{print $1 "|" $3}'`
# Liste des Revues
ListeR=`grep -E "^Ed.*\|" $PathData/$InfoPubli | sed -e "s/ /\&nbsp;/g"`

# Pour chaque ident de la base, on fait la mise en forme (MeF) des données
for j in $LISTE; do
  LitPubli $j
  MisFor=""

  # MeF Editeur
  EditI=`echo "$ListeR" | grep -E "^$EditC\|" | awk -F'|' '{print $2}'`;

  # Mef Liste des auteurs
  aux=""; tmp1=""
  for k in $AutrL; do
    tmp1="$tmp1, $aux"
    aux=`echo "$ListeA" | grep -E "^$k\|" | awk -F'|' '{print $2}'`;
  done
  if [ "$tmp1" = ", " ]; then tmp1="$aux."; else tmp1="${tmp1#, , } and $aux."; fi
  ## MisFor="$MisFor$tmp1|$Titre" 
  MisFor="$tmp1|$Titre" 

  # MeF Statut et references
  case $Statu in
	"Stsub") MisFor="$MisFor Submitted to $EditI.";;
	"Stinp") MisFor="$MisFor $EditI, In press.";;
	"Stacc") MisFor="$MisFor Accepted in $EditI.";;
          *) if [ "$PageD" = "0" ] && [ "$PageF" = "0" ]; then
		MisFor="$MisFor|$EditI,|$Volum"
	     else
	     	MisFor="$MisFor|$EditI,|$Volum:$PageD-$PageF"
	     fi ;;
  esac
  Abs=""; Prp="";

  # MeF Abstract
  if [ "$Abstr" != "Rsno" ]; then Extension "$Abstr"; FileDoc=$j"ab.$VarTmp"
    if [ -e $PathWeb$RelPath/documents/$FileDoc ]; then Abs="$FileDoc"; fi
  fi
  
  # MeF Pre-Print
  if [ "$PrPri" != "Ppno" ]; then Extension "$PrPri"; FileDoc=$j"pp.$VarTmp"
    if [ -e $PathWeb$RelPath/documents/$FileDoc ]; then Prp="$FileDoc"; fi
  fi
  ## MisFor="$MisFor ($Annee).$Abs$Prp<br><br></p>"

  # MeF ajout de la nouvelle ligne au fichier BaseModif
  ## echo "$Annee|$AutrL|$EditC|$DomRS|$MisFor|" >> $Basemodif
  echo "$Annee|$MisFor|$Abs|$Prp|" >> $Basemodif    
done

# Copie de Basemodif dans Data
\mv -f $WorkDir/$Basemodif $PathData/$Basemodif
}

#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------ Main -------------------------------------
#-------------------------------------------------------------------------------



## #Copie des nouveaux documents
## if [ -e $WorkDir/$TarDoc ]; then
##   \mv -f $WorkDir/$TarDoc $PathWeb$RelPath/documents
##   cd $PathWeb$RelPath/documents
##   tar xzf $TarDoc
##   \rm -f $TarDoc
## fi
## 
## # bck old et copie info-publi.dat, $PubliBase et tracemodif.dat
## cd $WorkDir
## if [ -e $InfoPubli ]; then 
##   \mv -f $PathData/$InfoPubli $PathData/$InfoPubli.old
##   \mv -f $InfoPubli $PathData
## fi
## 
## if [ -e $PubliBase ]; then 
##   \mv -f $PathData/$PubliBase $PathData/$PubliBase.old
##   \mv -f $PubliBase $PathData
## fi
## 
## if [ -e $TraceModif ]; then 
##   \mv -f $PathData/$TraceModif $PathData/$TraceModif.old
##   \mv -f $TraceModif $PathData
## fi


# Creation du fichier Basemodif
\rm -f $Basemodif
GenererBasemodif

# Creation du fichier BaseSearch
\rm -f $BaseSearch
GenererBaseSearch





