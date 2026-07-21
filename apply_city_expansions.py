import os
import re
import json

def apply_troy():
    fpath = 'troy-sewer-cleanup.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Meta Description if needed
    content = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="24/7 emergency sewer backup cleanup and sewage removal in Troy, MI. Fast 45-minute local response. Call 24/7: (248) 825-8312.">',
        content
    )

    # 2. Insert FAQPage Schema in head
    faq_schema = """
    <!-- JSON-LD FAQPage Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Does Troy's storm drainage system contribute to sewer backup risk?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Troy's Streets and Drains Division maintains an extensive storm water drainage network. In older sections near the Big Beaver corridor, heavy rain events can still overwhelm capacity faster than newer subdivisions, increasing backup risk."
          }
        },
        {
          "@type": "Question",
          "name": "What does sewage cleanup typically cost in Troy, MI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Emergency sewage cleanup in Troy ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+."
          }
        },
        {
          "@type": "Question",
          "name": "How long does structural drying take after a Troy basement backup?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Structural drying in Troy typically takes 3 to 5 days with industrial dehumidification and commercial air movers, depending on how much moisture was absorbed."
          }
        },
        {
          "@type": "Question",
          "name": "Is a sewer backup covered by standard homeowners insurance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy."
          }
        }
      ]
    }
    </script>
</head>"""
    content = content.replace('</head>', faq_schema)

    # 3. Body Copy Expansion
    troy_body = """                    <p class="text-sm text-gray-300 leading-relaxed">
                        Oakland County properties feature older subterranean utility corridors that are highly prone to tree root intrusions and blockages. When heavy rainfall hits, these drainage pipelines fail, backing up raw wastewater through residential basement floor drains. Immediate intervention is required to stop the wastewater from saturating drywall and framing.
                    </p>
                    <p class="text-sm text-gray-300 leading-relaxed">
                        Our certified technicians deploy professional truck-mounted vacuum systems to rapidly evacuate standing sewage. Once the wastewater is extracted, we remove saturated building components and sanitize the entire environment using EPA-registered biocides to eliminate viral hazards.
                    </p>

                    <!-- WHY TROY HOMES ARE AT HIGHER RISK -->
                    <div class="space-y-4 pt-2">
                        <h3 class="text-lg font-outfit font-bold text-white">Why Troy Homes Are at Higher Risk</h3>
                        <p class="text-sm text-gray-300 leading-relaxed">
                            Troy's neighborhoods span a wide range of housing ages, from 1950s–60s split-levels near Big Beaver Road to established subdivisions in areas like Northfield Hills. Many homes from this era still run on original clay tile or cast-iron sewer laterals — materials that develop interior scale and brittle joints over decades, giving tree roots an easy entry point. Troy's mature, tree-lined subdivisions compound this, while high water table conditions near the Big Beaver corridor increase flood risk during spring thaw and heavy summer storms.
                        </p>

                        <h4 class="text-sm font-bold text-white uppercase tracking-wider">Common Triggers We See in Troy:</h4>
                        <ul class="list-disc list-inside text-xs sm:text-sm text-gray-300 space-y-1.5 pl-2">
                            <li>Backups following spring thaw as frozen ground releases and shifts around aging pipe joints</li>
                            <li>Storm surges near the Big Beaver Road corridor overwhelming aging storm drainage</li>
                            <li>Root intrusion in older clay laterals throughout established subdivisions</li>
                            <li>Sump pump failures during high-water-table conditions common to lower-lying lots</li>
                        </ul>
                    </div>

                    <!-- WHAT TO DO IN THE FIRST 10 MINUTES -->
                    <div class="bg-red-950/40 border border-red-500/30 p-5 rounded-xl space-y-3 my-6">
                        <h3 class="text-base font-outfit font-extrabold text-red-400 uppercase tracking-wider">⚠️ What to Do in the First 10 Minutes of a Sewer Backup</h3>
                        <ol class="list-decimal list-inside text-xs sm:text-sm text-gray-200 space-y-2">
                            <li><strong>Stop using water immediately</strong> — do not run faucets, flush toilets, or run dishwashers/washing machines.</li>
                            <li><strong>Keep people and pets away</strong> — Category 3 black water carries harmful pathogens and bacteria on contact.</li>
                            <li><strong>Do not attempt to plunge or snake</strong> — household drain snakes can push contaminated water further into subflooring.</li>
                            <li><strong>Shut off electricity</strong> to the basement at the main breaker if it is safe to reach without stepping in standing water.</li>
                            <li><strong>Call for emergency extraction</strong> — rapid response within 45 minutes prevents long-term mold growth and framing rot.</li>
                        </ol>
                    </div>

                    <p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">
                        📍 <strong>Local Service Area:</strong> Our mobile response crews are stationed near the <a href="https://en.wikipedia.org/wiki/Big_Beaver_Road" target="_blank" rel="noopener noreferrer" class="text-red-400 hover:text-red-300 underline font-medium transition-colors">Big Beaver Road corridor</a>, Somerset Collection, and the Troy Historic Village area, ensuring immediate dispatch and a rapid 45-minute response time across Troy.
                    </p>

                    <!-- SECOND IMAGE SLOT -->
                    <div class="my-6">
                        <img src="/images/troy-sump-pump-repair.jpg" 
                             alt="Camera inspection and emergency sewage extraction equipment in Troy MI" 
                             title="Emergency Sewage Extraction & Camera Inspection Equipment Troy" 
                             class="w-full h-auto max-h-[300px] object-cover rounded-xl border border-slate-800 shadow-lg"
                             loading="lazy">
                        <p class="text-xs text-gray-400 text-center italic mt-2">Camera inspection helps identify root intrusion in Troy's older clay sewer laterals before a full backup occurs.</p>
                    </div>

                    <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-200 space-y-2">
                        <span class="block text-white font-bold uppercase tracking-wider">Decontamination Protocol:</span>
                        <p class="text-gray-300">We comply fully with industry standards for biological restoration. Raw sewage extraction is performed using closed-loop pump lines, ensuring dangerous sewage pathogens do not disperse into unaffected areas of your property. All disinfection procedures utilize EPA-registered hospital-grade antimicrobials, and we provide full moisture readings directly to your insurance provider.</p>
                    </div>"""

    old_body_pattern = r'<p class="text-sm text-gray-300 leading-relaxed">\s*Oakland County properties feature older subterranean utility corridors.*?</p>\s*<p class="text-sm text-gray-300 leading-relaxed">\s*Our certified technicians deploy.*?</p>\s*<p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">.*?</p>\s*<div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-400 space-y-2">.*?</div>'
    content = re.sub(old_body_pattern, troy_body, content, flags=re.DOTALL)

    # 4. Troy FAQ Accordion Section
    troy_faq = """        <!-- FAQ ACCORDION -->
        <section id="faq" class="py-16 bg-slate-900 px-4">
            <div class="max-w-3xl mx-auto">
                <h2 class="text-2xl font-outfit font-extrabold text-white text-center mb-10">Troy Frequently Asked Questions</h2>
                <div class="space-y-4">
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Does Troy's storm drainage system contribute to sewer backup risk?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Troy's Streets and Drains Division maintains an extensive storm water drainage network. In older sections near the Big Beaver corridor, heavy rain events can still overwhelm capacity faster than newer subdivisions, increasing backup risk.
                        </div>
                    </details>
                    
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>What does sewage cleanup typically cost in Troy, MI?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Emergency sewage cleanup in Troy ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>How long does structural drying take after a Troy basement backup?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Structural drying in Troy typically takes 3 to 5 days with industrial dehumidification and commercial air movers, depending on how much moisture was absorbed.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Is a sewer backup covered by standard homeowners insurance?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy. Our contracted partners document every single stage of the extraction process with digital photo logs and structural moisture mapping to make direct insurance billing as smooth as possible.
                        </div>
                    </details>
                </div>
            </div>
        </section>"""

    faq_pattern = r'<!-- FAQ ACCORDION -->\s*<section id="faq".*?</section>'
    content = re.sub(faq_pattern, troy_faq, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Troy page successfully.")

def apply_birmingham():
    fpath = 'birmingham-sewer-cleanup.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="24/7 emergency sewer backup cleanup and sewage removal in Birmingham, MI. Fast 45-minute local response. Call 24/7: (248) 825-8312.">',
        content
    )

    faq_schema = """
    <!-- JSON-LD FAQPage Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Are Birmingham's historic homes more prone to sewer backups?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Homes in Birmingham's historic sections often still have original cast-iron or clay sewer laterals. These older materials are more susceptible to root intrusion, corrosion, and joint failure over time."
          }
        },
        {
          "@type": "Question",
          "name": "What does sewage cleanup typically cost in Birmingham, MI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Emergency sewage cleanup in Birmingham ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+."
          }
        },
        {
          "@type": "Question",
          "name": "How long does a Birmingham basement take to dry out after a backup?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Basement drying in Birmingham typically takes 3 to 5 days using industrial air movers and dehumidifiers, depending on structural moisture saturation levels."
          }
        },
        {
          "@type": "Question",
          "name": "Is a sewer backup covered by standard homeowners insurance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy."
          }
        }
      ]
    }
    </script>
</head>"""
    content = content.replace('</head>', faq_schema)

    birmingham_body = """                    <p class="text-sm text-gray-300 leading-relaxed">
                        Oakland County properties feature older subterranean utility corridors that are highly prone to tree root intrusions and blockages. When heavy rainfall hits, these drainage pipelines fail, backing up raw wastewater through residential basement floor drains. Immediate intervention is required to stop the wastewater from saturating drywall and framing.
                    </p>
                    <p class="text-sm text-gray-300 leading-relaxed">
                        Our certified technicians deploy professional truck-mounted vacuum systems to rapidly evacuate standing sewage. Once the wastewater is extracted, we remove saturated building components and sanitize the entire environment using EPA-registered biocides to eliminate viral hazards.
                    </p>

                    <!-- WHY BIRMINGHAM HOMES ARE AT HIGHER RISK -->
                    <div class="space-y-4 pt-2">
                        <h3 class="text-lg font-outfit font-bold text-white">Why Birmingham Homes Are at Higher Risk</h3>
                        <p class="text-sm text-gray-300 leading-relaxed">
                            Birmingham's housing stock includes a significant share of homes from the late 19th and early 20th century, concentrated in historic districts and neighborhoods like Poppleton Park and the areas around Quarton Lake. These older homes commonly carry original cast-iron plumbing and sit on clay sewer laterals installed decades before modern PVC became standard. Birmingham's mature tree canopy means root intrusion is a frequent contributor to backups, especially in low-lying sections near Quarton Lake.
                        </p>

                        <h4 class="text-sm font-bold text-white uppercase tracking-wider">Common Triggers We See in Birmingham:</h4>
                        <ul class="list-disc list-inside text-xs sm:text-sm text-gray-300 space-y-1.5 pl-2">
                            <li>Backups in historic-district homes tied to original clay or cast-iron laterals</li>
                            <li>Root intrusion from mature trees along Birmingham's older residential streets</li>
                            <li>Heavy spring and fall rain events overwhelming aging storm and sanitary lines</li>
                            <li>Basement flooding near Quarton Lake and other low-lying residential sections</li>
                        </ul>
                    </div>

                    <!-- WHAT TO DO IN THE FIRST 10 MINUTES -->
                    <div class="bg-red-950/40 border border-red-500/30 p-5 rounded-xl space-y-3 my-6">
                        <h3 class="text-base font-outfit font-extrabold text-red-400 uppercase tracking-wider">⚠️ What to Do in the First 10 Minutes of a Sewer Backup</h3>
                        <ol class="list-decimal list-inside text-xs sm:text-sm text-gray-200 space-y-2">
                            <li><strong>Stop using water immediately</strong> — do not run faucets, flush toilets, or run dishwashers/washing machines.</li>
                            <li><strong>Keep people and pets away</strong> — Category 3 black water carries harmful pathogens and bacteria on contact.</li>
                            <li><strong>Do not attempt to plunge or snake</strong> — household drain snakes can push contaminated water further into subflooring.</li>
                            <li><strong>Shut off electricity</strong> to the basement at the main breaker if it is safe to reach without stepping in standing water.</li>
                            <li><strong>Call for emergency extraction</strong> — rapid response within 45 minutes prevents long-term mold growth and framing rot.</li>
                        </ol>
                    </div>

                    <p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">
                        📍 <strong>Local Service Area:</strong> Our mobile response crews are stationed near downtown Birmingham, Shain Park, and the <a href="https://en.wikipedia.org/wiki/Woodward_Avenue" target="_blank" rel="noopener noreferrer" class="text-red-400 hover:text-red-300 underline font-medium transition-colors">Woodward Avenue corridor</a>, ensuring immediate dispatch and a rapid 45-minute response time.
                    </p>

                    <!-- SECOND IMAGE SLOT -->
                    <div class="my-6">
                        <img src="/images/birmingham-sump-pump-repair.jpg" 
                             alt="Structural drying and sewage extraction equipment in Birmingham MI" 
                             title="Emergency Structural Drying & Sump Pump Equipment Birmingham" 
                             class="w-full h-auto max-h-[300px] object-cover rounded-xl border border-slate-800 shadow-lg"
                             loading="lazy">
                        <p class="text-xs text-gray-400 text-center italic mt-2">Structural drying equipment deployed after a Birmingham basement backup to prevent mold growth in original wood framing.</p>
                    </div>

                    <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-200 space-y-2">
                        <span class="block text-white font-bold uppercase tracking-wider">Decontamination Protocol:</span>
                        <p class="text-gray-300">We comply fully with industry standards for biological restoration. Raw sewage extraction is performed using closed-loop pump lines, ensuring dangerous sewage pathogens do not disperse into unaffected areas of your property. All disinfection procedures utilize EPA-registered hospital-grade antimicrobials, and we provide full moisture readings directly to your insurance provider.</p>
                    </div>"""

    old_body_pattern = r'<p class="text-sm text-gray-300 leading-relaxed">\s*Oakland County properties feature older subterranean utility corridors.*?</p>\s*<p class="text-sm text-gray-300 leading-relaxed">\s*Our certified technicians deploy.*?</p>\s*<p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">.*?</p>\s*<div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-400 space-y-2">.*?</div>'
    content = re.sub(old_body_pattern, birmingham_body, content, flags=re.DOTALL)

    birmingham_faq = """        <!-- FAQ ACCORDION -->
        <section id="faq" class="py-16 bg-slate-900 px-4">
            <div class="max-w-3xl mx-auto">
                <h2 class="text-2xl font-outfit font-extrabold text-white text-center mb-10">Birmingham Frequently Asked Questions</h2>
                <div class="space-y-4">
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Are Birmingham's historic homes more prone to sewer backups?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Homes in Birmingham's historic sections often still have original cast-iron or clay sewer laterals. These older materials are more susceptible to root intrusion, corrosion, and joint failure over time.
                        </div>
                    </details>
                    
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>What does sewage cleanup typically cost in Birmingham, MI?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Emergency sewage cleanup in Birmingham ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>How long does a Birmingham basement take to dry out after a backup?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Basement drying in Birmingham typically takes 3 to 5 days using industrial air movers and dehumidifiers, depending on structural moisture saturation levels.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Is a sewer backup covered by standard homeowners insurance?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy. Our contracted partners document every single stage of the extraction process with digital photo logs and structural moisture mapping to make direct insurance billing as smooth as possible.
                        </div>
                    </details>
                </div>
            </div>
        </section>"""

    faq_pattern = r'<!-- FAQ ACCORDION -->\s*<section id="faq".*?</section>'
    content = re.sub(faq_pattern, birmingham_faq, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Birmingham page successfully.")

def apply_berkley():
    fpath = 'berkley-sewer-cleanup.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="24/7 emergency sewer backup cleanup and sewage removal in Berkley, MI. Fast 45-minute local response. Call 24/7: (248) 825-8312.">',
        content
    )

    faq_schema = """
    <!-- JSON-LD FAQPage Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Does Berkley have a combined sewer system that increases backup risk?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Parts of Berkley's municipal sewer system handle both storm and sanitary flow together. During heavy rain, this can push more volume through the system than designed, increasing backup risk in older residential basements."
          }
        },
        {
          "@type": "Question",
          "name": "What does sewage cleanup typically cost in Berkley, MI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Emergency sewage cleanup in Berkley ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+."
          }
        },
        {
          "@type": "Question",
          "name": "How long does a Berkley basement take to dry out after a backup?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Basement drying in Berkley typically takes 3 to 5 days of industrial dehumidification, depending on how long water was standing and structural saturation."
          }
        },
        {
          "@type": "Question",
          "name": "Is a sewer backup covered by standard homeowners insurance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy."
          }
        }
      ]
    }
    </script>
</head>"""
    content = content.replace('</head>', faq_schema)

    berkley_body = """                    <p class="text-sm text-gray-300 leading-relaxed">
                        Oakland County properties feature older subterranean utility corridors that are highly prone to tree root intrusions and blockages. When heavy rainfall hits, these drainage pipelines fail, backing up raw wastewater through residential basement floor drains. Immediate intervention is required to stop the wastewater from saturating drywall and framing.
                    </p>
                    <p class="text-sm text-gray-300 leading-relaxed">
                        Our certified technicians deploy professional truck-mounted vacuum systems to rapidly evacuate standing sewage. Once the wastewater is extracted, we remove saturated building components and sanitize the entire environment using EPA-registered biocides to eliminate viral hazards.
                    </p>

                    <!-- WHY BERKLEY HOMES ARE AT HIGHER RISK -->
                    <div class="space-y-4 pt-2">
                        <h3 class="text-lg font-outfit font-bold text-white">Why Berkley Homes Are at Higher Risk</h3>
                        <p class="text-sm text-gray-300 leading-relaxed">
                            Berkley's housing stock is largely bungalow-style construction from the 1940s and 1950s, built with original clay or cast-iron sewer laterals that are reaching the end of their service life. Berkley sits within the Rouge River watershed, and its relatively flat topography means heavy rain has limited places to drain quickly. Combined with older municipal combined sewer lines, heavy rain events push extra wastewater volume back up through basement floor drains in older homes.
                        </p>

                        <h4 class="text-sm font-bold text-white uppercase tracking-wider">Common Triggers We See in Berkley:</h4>
                        <ul class="list-disc list-inside text-xs sm:text-sm text-gray-300 space-y-1.5 pl-2">
                            <li>Backups tied to Berkley's older combined storm/sanitary sewer sections during heavy rain</li>
                            <li>Root intrusion in clay sewer laterals common to 1940s–50s bungalow construction</li>
                            <li>Sump pump overload during multi-inch downpours in the Rouge River watershed area</li>
                            <li>Basement flooding affecting original hardwood floors and framing in older homes</li>
                        </ul>
                    </div>

                    <!-- WHAT TO DO IN THE FIRST 10 MINUTES -->
                    <div class="bg-red-950/40 border border-red-500/30 p-5 rounded-xl space-y-3 my-6">
                        <h3 class="text-base font-outfit font-extrabold text-red-400 uppercase tracking-wider">⚠️ What to Do in the First 10 Minutes of a Sewer Backup</h3>
                        <ol class="list-decimal list-inside text-xs sm:text-sm text-gray-200 space-y-2">
                            <li><strong>Stop using water immediately</strong> — do not run faucets, flush toilets, or run dishwashers/washing machines.</li>
                            <li><strong>Keep people and pets away</strong> — Category 3 black water carries harmful pathogens and bacteria on contact.</li>
                            <li><strong>Do not attempt to plunge or snake</strong> — household drain snakes can push contaminated water further into subflooring.</li>
                            <li><strong>Shut off electricity</strong> to the basement at the main breaker if it is safe to reach without stepping in standing water.</li>
                            <li><strong>Call for emergency extraction</strong> — rapid response within 45 minutes prevents long-term mold growth and framing rot.</li>
                        </ol>
                    </div>

                    <p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">
                        📍 <strong>Local Service Area:</strong> Our mobile response crews are stationed throughout Berkley's residential neighborhoods near 12 Mile Road, ensuring rapid dispatch across the city.
                    </p>

                    <!-- SECOND IMAGE SLOT -->
                    <div class="my-6">
                        <img src="/images/berkley-sump-pump-repair.jpg" 
                             alt="Emergency sewage extraction and structural drying in Berkley MI" 
                             title="Emergency Sewage Extraction & Sump Pump Equipment Berkley" 
                             class="w-full h-auto max-h-[300px] object-cover rounded-xl border border-slate-800 shadow-lg"
                             loading="lazy">
                        <p class="text-xs text-gray-400 text-center italic mt-2">Extraction crews work carefully around original hardwood and plaster common in Berkley's older bungalow homes.</p>
                    </div>

                    <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-200 space-y-2">
                        <span class="block text-white font-bold uppercase tracking-wider">Decontamination Protocol:</span>
                        <p class="text-gray-300">We comply fully with industry standards for biological restoration. Raw sewage extraction is performed using closed-loop pump lines, ensuring dangerous sewage pathogens do not disperse into unaffected areas of your property. All disinfection procedures utilize EPA-registered hospital-grade antimicrobials, and we provide full moisture readings directly to your insurance provider.</p>
                    </div>"""

    old_body_pattern = r'<p class="text-sm text-gray-300 leading-relaxed">\s*Oakland County properties feature older subterranean utility corridors.*?</p>\s*<p class="text-sm text-gray-300 leading-relaxed">\s*Our certified technicians deploy.*?</p>\s*<p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">.*?</p>\s*<div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-400 space-y-2">.*?</div>'
    content = re.sub(old_body_pattern, berkley_body, content, flags=re.DOTALL)

    berkley_faq = """        <!-- FAQ ACCORDION -->
        <section id="faq" class="py-16 bg-slate-900 px-4">
            <div class="max-w-3xl mx-auto">
                <h2 class="text-2xl font-outfit font-extrabold text-white text-center mb-10">Berkley Frequently Asked Questions</h2>
                <div class="space-y-4">
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Does Berkley have a combined sewer system that increases backup risk?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Parts of Berkley's municipal sewer system handle both storm and sanitary flow together. During heavy rain, this can push more volume through the system than designed, increasing backup risk in older residential basements.
                        </div>
                    </details>
                    
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>What does sewage cleanup typically cost in Berkley, MI?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Emergency sewage cleanup in Berkley ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>How long does a Berkley basement take to dry out after a backup?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Basement drying in Berkley typically takes 3 to 5 days of industrial dehumidification, depending on how long water was standing and structural saturation.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Is a sewer backup covered by standard homeowners insurance?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy. Our contracted partners document every single stage of the extraction process with digital photo logs and structural moisture mapping to make direct insurance billing as smooth as possible.
                        </div>
                    </details>
                </div>
            </div>
        </section>"""

    faq_pattern = r'<!-- FAQ ACCORDION -->\s*<section id="faq".*?</section>'
    content = re.sub(faq_pattern, berkley_faq, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Berkley page successfully.")

def apply_clawson():
    fpath = 'clawson-sewer-cleanup.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="24/7 emergency sewer backup cleanup and sewage removal in Clawson, MI. Fast 45-minute local response. Call 24/7: (248) 825-8312.">',
        content
    )

    faq_schema = """
    <!-- JSON-LD FAQPage Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why are Clawson's older bungalow homes more prone to sewer backups?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Clawson's housing stock is predominantly 1930s-1950s brick bungalows running on original clay or cast-iron sewer laterals. Decades of root intrusion and internal corrosion make these older lines more susceptible to blockages and backups during heavy rain."
          }
        },
        {
          "@type": "Question",
          "name": "What does sewage cleanup typically cost in Clawson, MI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Emergency sewage cleanup in Clawson ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+."
          }
        },
        {
          "@type": "Question",
          "name": "How long does a Clawson basement take to dry out after a backup?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Basement drying in Clawson typically takes 3 to 5 days using industrial air movers and dehumidifiers, depending on how long water was standing."
          }
        },
        {
          "@type": "Question",
          "name": "Is a sewer backup covered by standard homeowners insurance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy."
          }
        }
      ]
    }
    </script>
</head>"""
    content = content.replace('</head>', faq_schema)

    clawson_body = """                    <p class="text-sm text-gray-300 leading-relaxed">
                        Oakland County properties feature older subterranean utility corridors that are highly prone to tree root intrusions and blockages. When heavy rainfall hits, these drainage pipelines fail, backing up raw wastewater through residential basement floor drains. Immediate intervention is required to stop the wastewater from saturating drywall and framing.
                    </p>
                    <p class="text-sm text-gray-300 leading-relaxed">
                        Our certified technicians deploy professional truck-mounted vacuum systems to rapidly evacuate standing sewage. Once the wastewater is extracted, we remove saturated building components and sanitize the entire environment using EPA-registered biocides to eliminate viral hazards.
                    </p>

                    <!-- WHY CLAWSON HOMES ARE AT HIGHER RISK -->
                    <div class="space-y-4 pt-2">
                        <h3 class="text-lg font-outfit font-bold text-white">Why Clawson Homes Are at Higher Risk</h3>
                        <p class="text-sm text-gray-300 leading-relaxed">
                            Clawson's housing stock is predominantly brick bungalows built between the 1930s and 1950s on compact city lots. Homes of this era commonly run on original clay or cast-iron sewer laterals, which after decades of use are prone to root intrusion at pipe joints and internal corrosion that narrows usable pipe diameter. Heavy regional storm events in southeast Oakland County put extra strain on older sanitary infrastructure, contributing to Category 3 sewer-backup exposure during rainstorms.
                        </p>

                        <h4 class="text-sm font-bold text-white uppercase tracking-wider">Common Triggers We See in Clawson:</h4>
                        <ul class="list-disc list-inside text-xs sm:text-sm text-gray-300 space-y-1.5 pl-2">
                            <li>Root intrusion through clay pipe joints common to 1930s–50s bungalow construction</li>
                            <li>Internal corrosion in older cast-iron lines reducing effective pipe capacity</li>
                            <li>Backups following heavy regional rain events that overwhelm aging sanitary lines</li>
                            <li>Compact lot layouts requiring specialized mobile equipment staging</li>
                        </ul>
                    </div>

                    <!-- WHAT TO DO IN THE FIRST 10 MINUTES -->
                    <div class="bg-red-950/40 border border-red-500/30 p-5 rounded-xl space-y-3 my-6">
                        <h3 class="text-base font-outfit font-extrabold text-red-400 uppercase tracking-wider">⚠️ What to Do in the First 10 Minutes of a Sewer Backup</h3>
                        <ol class="list-decimal list-inside text-xs sm:text-sm text-gray-200 space-y-2">
                            <li><strong>Stop using water immediately</strong> — do not run faucets, flush toilets, or run dishwashers/washing machines.</li>
                            <li><strong>Keep people and pets away</strong> — Category 3 black water carries harmful pathogens and bacteria on contact.</li>
                            <li><strong>Do not attempt to plunge or snake</strong> — household drain snakes can push contaminated water further into subflooring.</li>
                            <li><strong>Shut off electricity</strong> to the basement at the main breaker if it is safe to reach without stepping in standing water.</li>
                            <li><strong>Call for emergency extraction</strong> — rapid response within 45 minutes prevents long-term mold growth and framing rot.</li>
                        </ol>
                    </div>

                    <p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">
                        📍 <strong>Local Service Area:</strong> Our mobile response crews are stationed throughout Clawson's residential neighborhoods near 14 Mile Road, ensuring rapid dispatch across the city.
                    </p>

                    <!-- SECOND IMAGE SLOT -->
                    <div class="my-6">
                        <img src="/images/clawson-sump-pump-repair.jpg" 
                             alt="Emergency sewage extraction and sump pump equipment in Clawson MI" 
                             title="Emergency Sewage Extraction & Sump Pump Equipment Clawson" 
                             class="w-full h-auto max-h-[300px] object-cover rounded-xl border border-slate-800 shadow-lg"
                             loading="lazy">
                        <p class="text-xs text-gray-400 text-center italic mt-2">Clawson's compact lots and narrow driveways require crews experienced with tight equipment staging.</p>
                    </div>

                    <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-200 space-y-2">
                        <span class="block text-white font-bold uppercase tracking-wider">Decontamination Protocol:</span>
                        <p class="text-gray-300">We comply fully with industry standards for biological restoration. Raw sewage extraction is performed using closed-loop pump lines, ensuring dangerous sewage pathogens do not disperse into unaffected areas of your property. All disinfection procedures utilize EPA-registered hospital-grade antimicrobials, and we provide full moisture readings directly to your insurance provider.</p>
                    </div>"""

    old_body_pattern = r'<p class="text-sm text-gray-300 leading-relaxed">\s*Oakland County properties feature older subterranean utility corridors.*?</p>\s*<p class="text-sm text-gray-300 leading-relaxed">\s*Our certified technicians deploy.*?</p>\s*<p class="text-xs sm:text-sm text-gray-300 leading-relaxed italic border-l-2 border-red-600 pl-3 bg-slate-950/20 py-2">.*?</p>\s*<div class="bg-slate-900 border border-slate-800 p-5 rounded-xl text-xs text-gray-400 space-y-2">.*?</div>'
    content = re.sub(old_body_pattern, clawson_body, content, flags=re.DOTALL)

    clawson_faq = """        <!-- FAQ ACCORDION -->
        <section id="faq" class="py-16 bg-slate-900 px-4">
            <div class="max-w-3xl mx-auto">
                <h2 class="text-2xl font-outfit font-extrabold text-white text-center mb-10">Clawson Frequently Asked Questions</h2>
                <div class="space-y-4">
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Why are Clawson's older bungalow homes more prone to sewer backups?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Clawson's housing stock is predominantly 1930s-1950s brick bungalows running on original clay or cast-iron sewer laterals. Decades of root intrusion and internal corrosion make these older lines more susceptible to blockages and backups during heavy rain.
                        </div>
                    </details>
                    
                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>What does sewage cleanup typically cost in Clawson, MI?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Emergency sewage cleanup in Clawson ranges between $400 and $1,500 for initial wastewater extraction and biological containment, while extensive black-water flood damage requiring multi-room structural drying can reach $3,000+.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>How long does a Clawson basement take to dry out after a backup?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            Basement drying in Clawson typically takes 3 to 5 days using industrial air movers and dehumidifiers, depending on how long water was standing.
                        </div>
                    </details>

                    <details class="group border border-slate-800 rounded-xl bg-slate-950/40 overflow-hidden">
                        <summary class="flex items-center justify-between p-5 text-white font-outfit font-bold text-base cursor-pointer hover:bg-slate-900/50 transition-colors list-none">
                            <span>Is a sewer backup covered by standard homeowners insurance?</span>
                            <span class="transition group-open:rotate-180 text-red-500 font-bold shrink-0 ml-4">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                            </span>
                        </summary>
                        <div class="p-5 border-t border-slate-800/60 text-xs text-gray-300 leading-relaxed bg-slate-950/20">
                            In most scenarios, yes—provided you have a 'Sewer Backup and Sump Pump Overflow' rider attached to your property policy. Our contracted partners document every single stage of the extraction process with digital photo logs and structural moisture mapping to make direct insurance billing as smooth as possible.
                        </div>
                    </details>
                </div>
            </div>
        </section>"""

    faq_pattern = r'<!-- FAQ ACCORDION -->\s*<section id="faq".*?</section>'
    content = re.sub(faq_pattern, clawson_faq, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Clawson page successfully.")

if __name__ == "__main__":
    apply_troy()
    apply_birmingham()
    apply_berkley()
    apply_clawson()
