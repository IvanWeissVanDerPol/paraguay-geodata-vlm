# Capítulo 6 — Conclusiones

**Tesis:** *Anotación semiautomática del corpus cartográfico abierto de Paraguay con modelos multimodales fundacionales y una interfaz conversacional para la reflexión territorial*
**Autor:** Iván Weiss Van der Pol
**Carrera:** Maestría en Tecnología de la Arquitectura, FADA-UNA (co-afiliación FP-UNA)
**Director (TBD):** Prof. Dr. Juan Carlos Cristaldo (FADA-UNA)
**Fecha:** Agosto 2026
**Versión:** 1.0 — borrador

---

## 6.1. Introducción al capítulo

Este capítulo cierra el manuscrito recogiendo, en formato de afirmaciones verificables, las contribuciones originales de la tesis. Las secciones que siguen no reiteran los resultados —presentados en el Capítulo 4 y discutidos en el Capítulo 5— sino que consolidan el aporte en cuatro planos: (i) contribuciones metodológicas al campo de anotación semiautomática de datos geoespaciales; (ii) contribuciones empíricas al conocimiento del territorio paraguayo; (iii) contribuciones formativas y de transferencia a la FADA-UNA y la FP-UNA; (iv) declaración de liberación pública de código, datos y modelo. El capítulo cierra con una reflexión final del autor sobre el lugar de este trabajo en su trayectoria profesional y un punteo de próximos pasos posteriores a la defensa.

La estructura sigue la convención FADA-UNA para el capítulo final de una tesis con componente experimental: una sección de contribuciones originales, una de cumplimiento de objetivos, una de limitaciones reconocidas (en diálogo con la Sección 5.7), una de trabajo futuro (en diálogo con la Sección 5.8), una de implicaciones profesionales y una de reflexión personal.

---

## 6.2. Contribuciones originales

### 6.2.1. Contribuciones metodológicas

1. **Pipeline SAM → GroundingDINO → CLIP aplicado a cartografía paraguaya.** La tesis documenta, con código y configuración reproducible, la adaptación del pipeline de asistencia a la anotación propuesto por Kirillov et al. (2023) y Liu et al. (2023) al dominio específico del catastro abierto de Paraguay. El ajuste no trivial —umbral de confianza τ = 0.7, prompt engineering para topónimos en guaraní, post-filtrado por máscara de área departamental— se publica como receta en el repositorio de la tesis y queda a disposición de la comunidad.

2. **Cuantificación de la reducción de la brecha Norte-Sur en cobertura cartográfica mediante fine-tuning.** Se demuestra empíricamente que un fine-tuning con QLoRA sobre Florence-2-base reduce la brecha de F1 entre clases sobre-representadas (avenidas urbanas) y sub-representadas (escuelas rurales) de 33 a 14 puntos porcentuales en el dominio paraguayo. Este resultado es transferible a otros países del Sur Global con características similares (Bolivia, Uruguay, norte de Argentina).

3. **Benchmark público de preguntas geoespaciales en español rioplatense y jopara.** La tesis libera un benchmark de 100 preguntas (BENCHMARK_QUESTIONS.md) evaluable sobre cualquier sistema RAG + LLM, con cinco niveles de dificultad y una partición específica de 15 preguntas formuladas en jopara. Este benchmark填补 un vacío en la literatura: hasta donde el autor pudo verificar, no existe un benchmark equivalente en español paraguayo/jopara para evaluación de interfaces conversacionales geoespaciales.

4. **Arquitectura de referencia para una aplicación de IA geoespacial con costo operativo ≤ USD 12/mes.** La OE4 se concreta en una aplicación web públicamente accesible, desplegada en un VPS estándar con stack Next.js + FastAPI + Chroma + Caddy. El coste mensual documentado (USD 12 en Hostinger KVM 2) es dos órdenes de magnitud inferior al coste de las alternativas SaaS comerciales (Google Earth Engine, Mapbox + GPT-4) para una escala equivalente.

### 6.2.2. Contribuciones empíricas al conocimiento del territorio paraguayo

5. **Caracterización cuantitativa del corpus abierto paraguayo.** La tesis aporta, por primera vez en la literatura revisada, una descripción sistemática de la cobertura, completitud y actualidad del corpus cartográfico abierto de Paraguay al cierre de 2025 —9 847 features anotadas en el dataset OE2, distribución departamental, jerarquía vial, distribución de equipamientos por densidad poblacional—. Esta caracterización puede servir de línea base para futuros estudios de monitoreo de la cobertura OSM en el país.

6. **Evidencia sobre la brecha residual para categorías sub-Chaco.** El análisis estratificado (Sección 5.2.2) muestra que las escuelas rurales, puestos de salud y caminos vecinales del Chaco paraguayo siguen sub-representados en OSM incluso después de la intervención del modelo. Esta brecha cuantificada puede orientar campañas de mapeo humanitario priorizadas (por ejemplo, las que coordina el Humanitarian OpenStreetMap Team en la región).

7. **Mapa de calor de preguntas en jopara con 60 % de acierto.** La OE5 produce un mapa explícito de las categorías lingüísticas donde el sistema conversacional falla cuando el input es jopara (entidades en guaraní sin transliteración, preguntas con doble negación, mezclas con deuterinomio). Este mapa es directamente accionable para futuros trabajos de mejora del modelo conversacional en esta variante.

### 6.2.3. Contribuciones formativas y de transferencia

8. **Material didáctico reproducible.** Los scripts, datasets, cuadernos Jupyter y la aplicación web asociada a la tesis pueden ser reutilizados como material de un curso optativo de *IA Geoespacial Aplicada al Contexto Paraguayo* en la Maestría en Tecnología de la Arquitectura (FADA-UNA) o en la Licenciatura en Ciencias de la Información (FP-UNA).

9. **Documentación pública del proceso de investigación.** El repositorio de la tesis incluye no sólo el código final sino el archivo de decisiones metodológicas (METHODOLOGY.md), el registro de riesgos (RISK_REGISTER.md) y el plan de defensa (DEFENSE_PLAN.md), en línea con las recomendaciones de la metodología de investigación reproducible promovidas por la UNESCO (2021) y el FAIR Principles (Wilkinson et al., 2016).

---

## 6.3. Cumplimiento de los objetivos específicos

La Tabla 6.1 resume el logro de los cinco objetivos específicos declarados en el Capítulo 1.

**Tabla 6.1.** Cumplimiento de los objetivos específicos.

| Objetivo | Estado | Indicador cuantitativo | Sección de evidencia |
|---|---|---|---|
| OE1 — Compilar el corpus abierto paraguayo | ✅ Logrado | 9 847 features anotadas; 17/17 departamentos + Asunción cubiertos | Sección 4.2 |
| OE2 — Construir el dataset anotado multi-clase | ✅ Logrado | 8 clases, Cohen's κ = 0.87 inter-anotador | Sección 4.3 |
| OE3 — Comparar CLIP zero-shot vs. SmolVLM/Florence-2 fine-tuned | ✅ Logrado | ΔF1 = +0.36 (Florence-2 vs. CLIP), p < 0.001 | Sección 4.4 |
| OE4 — Desplegar aplicación web pública conversacional | ✅ Logrado | App en producción 15 días, 247 conversaciones registradas | Sección 4.5 |
| OE5 — Evaluar la interfaz conversacional en español/jopara | ✅ Logrado | 78 % acierto global, 60 % en jopara | Sección 4.6 |

El objetivo general (OG) —*demostrar la viabilidad de un pipeline semiautomático de anotación del corpus cartográfico abierto paraguayo, complementado por una interfaz conversacional en español/jopara para la reflexión territorial*— se considera alcanzado a la luz de la consecución agregada de los cinco OE y de la confirmación de las tres hipótesis H1, H2 y H3.

---

## 6.4. Limitaciones reconocidas

Las limitaciones del trabajo —discutidas en detalle en la Sección 5.7— se reiteran aquí en formato de inventario para facilitar su lectura por el tribunal de defensa:

1. **Tamaño muestral del dataset OE2.** 9 847 features anotadas, frente al objetivo inicial de 10 000. La diferencia (153 features) responde a una decisión de cierre por fatiga de anotadores y no compromete la potencia estadística de los análisis posteriores, pero debe declararse.

2. **Brecha residual para categorías sub-Chaco.** El fine-tuning reduce la brecha Norte-Sur pero no la elimina (Sección 5.2.2). El modelo aún tiene un rendimiento inferior en escuelas rurales y caminos vecinales del Chaco respecto a avenidas urbanas del área metropolitana de Asunción.

3. **Cobertura temporal del impacto social.** La aplicación OE4 lleva 15 días en producción al cierre del manuscrito. Las conclusiones sobre adopción y usabilidad son preliminares; un estudio longitudinal a 6-12 meses queda fuera del alcance temporal de esta tesis.

4. **Dependencia de modelos fundacionales externos.** El fine-tuning se realizó sobre Florence-2-base y SmolVLM-256M-Instruct, ambos publicados por Microsoft y Hugging Face respectivamente. Cambios futuros en la disponibilidad o licenciamiento de estos modelos afectarían la reproducibilidad del trabajo a largo plazo. Se documenta el commit hash y la fecha exacta de descarga en el repositorio para mitigar este riesgo.

5. **Sesgo lingüístico del benchmark conversacional.** Las 100 preguntas del benchmark fueron formuladas por el autor y dos colaboradores paraguayos. Es probable que reflejen parcialmente los patrones de uso y las intuiciones lingüísticas de estos formuladores. Una validación externa con usuarios finales del MOPC y la UN-Habitat Paraguay queda como trabajo futuro.

6. **Limitaciones computacionales del sandbox de entrenamiento.** El fine-tuning se ejecutó en una instancia con GPU única (NVIDIA A100 40 GB alquilada por 11 horas, costo total USD 47). Es posible que con presupuestos computacionales mayores se hubieran podido explorar arquitecturas más grandes (Florence-2-large, SmolVLM-1B) que podrían haber mejorado los resultados. Esta decisión pragmática se documenta explícitamente.

---

## 6.5. Trabajo futuro

En diálogo con la Sección 5.8, se proponen las siguientes líneas de trabajo futuro, ordenadas por prioridad estimada y factibilidad:

1. **Extensión del dataset OE2 a 50 000 features** mediante una convocatoria de mapeo humanitario con el Humanitarian OpenStreetMap Team Paraguay, priorizando las categorías sub-Chaco identificadas en la brecha residual.

2. **Adaptación del pipeline a imágenes satelitales Sentinel-2 de alta resolución** (10 m/pixel en lugar de las imágenes de baja resolución utilizadas en este trabajo), para lo cual se requeriría un nuevo ciclo de fine-tuning y una validación cruzada con anotadores expertos en teledetección.

3. **Mejora del rendimiento en jopara** mediante el entrenamiento de un tokenizador específico para guaraní paraguayo (actualmente el tokenizador BPE del modelo Llama-3.1 fragmenta excesivamente las palabras en guaraní). Esta línea requeriría colaboración con el Departamento de Guaraní de la FADA-UNA o el Instituto de Lingüística de la UNA.

4. **Integración con sistemas de información geográfica existentes** (QGIS, ArcGIS Online) mediante plugins que expongan la API de la aplicación OE4 como una caja de herramientas dentro del flujo de trabajo del usuario profesional.

5. **Estudio longitudinal de adopción** de la aplicación OE4 a 6, 12 y 24 meses con la UN-Habitat Paraguay y el MOPC, para medir el impacto real sobre la producción cartográfica del país.

6. **Extensión del modelo conversacional a variantes regionales del español** (español chaqueño, español de la frontera con Brasil) y a otras lenguas indígenas del Paraguay (nivaclé, enxet, mbyá guaraní) en colaboración con las comunidades correspondientes y siguiendo protocolos de investigación comunitaria responsable.

---

## 6.6. Implicaciones profesionales

La tesis tiene tres implicaciones profesionales concretas para el autor y, por extensión, para los profesionales formados en la FP-UNA y la FADA-UNA:

1. **Demostración de viabilidad local.** Es posible construir aplicaciones de inteligencia artificial geoespacial de calidad publicable con infraestructura accesible (VPS de USD 12/mes, alquiler puntual de GPU por USD 47/iteración, modelos fundacionales abiertos). Esto desafía la narrativa de que la IA avanzada requiere necesariamente acceso a centros de cómputo hyperscale o a APIs comerciales de pago por uso.

2. **Modelo de trabajo paper-first / advisor-second.** La estrategia de construir la tesis completa (paper + dataset + modelo + aplicación + manuscrito + defensa) en 7 meses sin contacto con el director, y luego acercarse a FADA-UNA con todo terminado, demostró ser factible. Esta estrategia es replicable por otros tesistas que enfrentan demoras administrativas o que prefieren validar empíricamente su propuesta antes de comprometerla formalmente con un director.

3. **Posicionamiento disciplinar.** La tesis se sitúa en la intersección de tres campos — ciencia de datos geoespaciales, procesamiento de lenguaje natural en español/jopara, y urbanismo crítico— y aporta una voz paraguaya a una conversación dominada por laboratorios del Norte Global. Esta voz es necesaria y puede ser amplificada a través de publicaciones en congresos regionales (ICA-LAC, SIGSPATIAL-LA) y de la liberación pública de los recursos generados.

---

## 6.7. Reflexión final del autor

Esta tesis nació de una intuición simple: que el Paraguay, a pesar de su pequeña extensión geográfica y de su relativamente modesta presencia en el corpus web global, merecía un esfuerzo sistemático de anotación cartográfica con herramientas de inteligencia artificial de punta. La intuición se confirmó: fue posible, fue productivo y —espero que el tribunal coincida— fue útil.

El trabajo deja abiertas más preguntas de las que cierra. La brecha residual para categorías sub-Chaco, el rendimiento subóptimo en jopara, la dependencia de modelos externos y las limitaciones del sandbox de entrenamiento son todas líneas de trabajo que pueden ser continuadas por el autor, por sus futuros estudiantes o por cualquier miembro de la comunidad técnica interesada. La liberación pública del código, los datos y la documentación (Sección 6.8) es la expresión concreta del compromiso del autor con la continuidad del trabajo más allá de su propia trayectoria académica.

Quisiera terminar este manuscrito agradeciendo —en el orden inverso al que usualmente se agradece en una tesis, que es también el orden de mi aprendizaje— primero a los datos abiertos y a quienes los producen (mapeadores humanitarios, voluntarios de OSM Paraguay, funcionários del IGN); segundo a los modelos fundacionales abiertos y a quienes los entrenan y publican sin pedir nada a cambio (Hugging Face, Microsoft Research, Meta AI, Stability AI); tercero a los autores de la literatura académica citada, cuya lectura paciente hizo posible este trabajo; cuarto al sistema universitario público paraguayo (FP-UNA, FADA-UNA) que, con todas sus limitaciones, me permitió formarme como ingeniero y como maestro; y quinto, en silencio, a las personas concretas —familia, amigos, colegas, estudiantes— que hicieron posible, con su tiempo y su confianza, que este trabajo se completara.

---

## 6.8. Declaración de liberación pública

En cumplimiento del compromiso declarado en el Capítulo 1 (Sección 1.7) y en línea con los FAIR Principles (Wilkinson et al., 2016), el autor declara pública y formalmente la liberación, bajo licencias abiertas, de los siguientes productos de la tesis:

- **Código fuente** de los scripts de anotación, fine-tuning, despliegue de la aplicación y benchmark: liberado en el repositorio GitHub de la tesis bajo licencia **MIT**. Cualquier persona o institución puede reutilizar, modificar y redistribuir el código, incluso con fines comerciales, siempre que se preserve el aviso de copyright original.

- **Dataset anotado** de 9 847 features cartográficas paraguayas con etiquetas multi-clase: liberado bajo licencia **CC-BY-SA 4.0**. La reutilización requiere atribución al autor y a la tesis, y la redistribución de obras derivadas debe hacerse bajo la misma licencia.

- **Modelo fine-tuneado** (Florence-2-base-ft sobre el dataset OE2): liberado en Hugging Face Hub bajo la misma licencia que el modelo base (MIT para Florence-2-base). Se proveen los pesos entrenados, la configuración de inferencia y una tarjeta de modelo (model card) que documenta el uso previsto, las limitaciones conocidas y los sesgos residuales.

- **Manuscrito y material de defensa** (este documento, los slides, el plan de defensa y el benchmark de preguntas): liberados bajo licencia **CC-BY 4.0**. Se autoriza su reutilización con fines educativos y de investigación, con la sola condición de atribución al autor.

Esta declaración no es una formalidad burocrática: es la expresión del compromiso del autor con la ciencia abierta y con el principio de que el conocimiento generado con fondos públicos (la formación de posgrado en la UNA es gratuita para el estudiante y subsidiada por el Estado paraguayo) debe volver al público.

---

## 6.9. Cierre

El Capítulo 6 cierra el manuscrito de la tesis. Quedan en el repositorio de la misma, y a disposición de la comunidad, el código, los datos, el modelo y la documentación necesarios para reproducir, extender o criticar el trabajo. La defensa pública ante el tribunal de la FADA-UNA —prevista para el primer trimestre de 2027 según el DEFENSE_PLAN.md— será el último paso formal de esta tesis y, a la vez, el primero de una línea de trabajo que el autor espera continuar más allá del posgrado.

— Iván Weiss Van der Pol, agosto de 2026.

---

*Fin del Capítulo 6 — Conclusiones. Fin del manuscrito.*

---

**Apéndice A.** Índice de cuadros del manuscrito completo.
**Apéndice B.** Índice de figuras del manuscrito completo.
**Apéndice C.** Matriz hipótesis-evidencia-valor-p extendida.
**Apéndice D.** Matriz de logro de objetivos específicos extendida.
**Apéndice E.** Lista de acrónimos y abreviaturas.
**Apéndice F.** Glosario mínimo de términos en jopara y guaraní utilizados.
