Intro til python fra blokkodning  
=======

For at introducere python og for piraterne til at blive vante til pythons syntaks osv. introducerede vi det gennem nogle hourofcode eksempler som de så skulle replikere med python og turtle.

Eleverne skal have installeret en eller anden editor og python, f.eks. visual studiocode. Eller en IDE som f.eks. Thonny.

Turtle er med i python standard bibliotek, så ingen problemer der.  

Det er en god ide at introducere hvordan man skriver et program og nogle af de basale turtle kommandoer inden man slipper piraterne løs.

Derefter leder man dem bare hen på [hour of code opgaven.](https://studio.code.org/s/frozen/stage/1/puzzle/1).
 
Hvor de så bare skal lave et program i turtle der kan det samme. Hvor man så introducere loops, funktioner... og sådan noget sideløbende.
Funktioner introduceres ved opg. 18 (altså så man laver en funktion for snefnug grenen).
Den kunne se sådan her ud:

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">snefnuggren</span>(): 
    antal_grene <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">3</span> 
    turtle<span style="color: #333333">.</span>forward((antal_grene)<span style="color: #333333">*</span><span style="color: #0000DD; font-weight: bold">10</span>) 
    <span style="color: #008800; font-weight: bold">for</span> gren <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(antal_grene): 
        turtle<span style="color: #333333">.</span>right(<span style="color: #0000DD; font-weight: bold">30</span>) 
        turtle<span style="color: #333333">.</span>forward(<span style="color: #0000DD; font-weight: bold">10</span>) 
        turtle<span style="color: #333333">.</span>backward(<span style="color: #0000DD; font-weight: bold">10</span>) 
        turtle<span style="color: #333333">.</span>left(<span style="color: #0000DD; font-weight: bold">30</span>) 
        turtle<span style="color: #333333">.</span>forward(<span style="color: #0000DD; font-weight: bold">10</span>) 
        turtle<span style="color: #333333">.</span>backward(<span style="color: #0000DD; font-weight: bold">10</span>) 
        turtle<span style="color: #333333">.</span>left(<span style="color: #0000DD; font-weight: bold">30</span>) 
        turtle<span style="color: #333333">.</span>forward(<span style="color: #0000DD; font-weight: bold">10</span>) 
        turtle<span style="color: #333333">.</span>backward(<span style="color: #0000DD; font-weight: bold">10</span>) 
        turtle<span style="color: #333333">.</span>right(<span style="color: #0000DD; font-weight: bold">30</span>) 
        turtle<span style="color: #333333">.</span>backward(<span style="color: #0000DD; font-weight: bold">10</span>)
</pre></div>
