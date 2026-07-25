# When Not to Use a Model

Most writing about AI in clinical work argues over which model to reach for. I spend more of my time on the opposite question. I'm a psychiatric nurse practitioner who builds the automation that runs my own practice, and the judgment that has paid off most is knowing when to take the model out of a step entirely. Three times in the past year I ripped an LLM out of a workflow and put a deterministic local script in its place. Each time the trigger was the same: the requirement had quietly stopped being a judgment call and become a guarantee. Here is what that cost, what it bought, and where I left the model exactly where it was.

## Case 1: Records intake

Patient record bundles arrive as zip archives. My first version of this workflow was a prompt. I would hand the archive to an AI assistant and tell it to open the file, read every document inside, and summarize what mattered before the visit.

It worked, mostly, which is the dangerous kind of working. The instruction was forgettable — some days I ran it, some days I meant to. Worse, it was unverifiable. Nothing about the process could tell me that every file in the bundle had actually been opened. A model that reads nine of ten documents produces output that looks exactly like a model that read all ten. In a records bundle, the tenth document is the one with the discharge note nobody mentioned on the phone. A missed file there is a clinical safety problem wearing the costume of a UX annoyance.

So I replaced the prompt with a local script. It unpacks the archive, runs OCR on everything inside, and emits a manifest that enumerates every file it processed. The guarantee moved from "I remembered to ask, and I trust the model read all of it" to "the manifest lists the file or it doesn't." I can look at the manifest count and know. There is no fluent summary standing between me and the ground truth.

The script picked up a second job I hadn't planned for. Part of what it does is relocate the incoming archive out of a cloud-synced folder that was never an approved location for that class of data, and into one that is. A prompt can be told to respect that boundary. It cannot enforce it, because it never touches the filesystem — it only describes intentions about one. A script moves the bytes. The boundary became a line of code, and code is the only kind of promise a computer keeps on its own.

## Case 2: Batch registration

Registering a long list of patients in a lab-ordering system, one at a time through a web UI, is slow and error-prone in the specific way repetitive work is error-prone: the mistakes cluster around the moment your attention lapses.

An LLM-driven browser agent can do this. I built one, and it worked in the demo. The problem showed up in production, where every run is a fresh roll of the dice. The agent clicks a slightly different path, a field renders half a second late, a dropdown has one more option than last time — and now I have a failure that requires forensic reconstruction to understand. What did it click? What state was the page in? Did it register forty-one patients or thirty-nine? Nondeterminism is tolerable when the output is a draft. It is corrosive when the output is a set of records I have to trust.

The replacement is boring, and boring is the point. Export the list to CSV. Run a local script against the vendor's API. Same output, every time. When something is wrong — a malformed row, a field the API rejects — the script fails loudly and points at the row, rather than improvising around the problem and leaving me to discover it later. It is auditable, because the CSV and the script together are a complete record of what was sent. It is re-runnable, because running it twice with the same input is safe. The browser agent had none of those properties, and no amount of prompt engineering was going to give it them.

## Case 3: Output validation

This is the failure mode that changed how I think about the whole category. I generate transcripts of clinical lectures using automated speech-to-text. The transcripts fail silently.

Not "fail" in the sense of throwing an error or flagging low confidence. They return fluent, grammatical, confident English — with the domain terms phonetically mangled into plausible nonsense. A drug name becomes a different real word that sounds like it and means nothing. There is no error code, no confidence bar dipping into the red, no ragged output that signals "check this." The transcript reads clean. That is precisely what makes it dangerous: the surface gives you no reason to look closer, and the mistakes are buried in exactly the terms a clinician needs to be right.

The instinct is to reach for a better model. That instinct is wrong here. A better model raises average accuracy and still leaves the misses silent; what I need is an alarm, and average accuracy does not provide one. So the fix is a deterministic check that sits after the transcription step. It scores the output against the domain vocabulary the topic predicts. A lecture on a given class of medication should contain a recognizable density of that class's terms; when the score falls below a threshold, the check refuses the transcript instead of passing it downstream. It doesn't try to fix the text. It just declines to pretend the text is fine. A gate that can say "no" is worth more than a model that is slightly more likely to say the right thing and gives you no way to tell when it didn't.

## Where the model stayed

None of this is an argument against LLMs, and I want to be precise about where I kept them, because the boundary is the whole point.

The model stayed everywhere the output is a draft that a human reads before it matters. It writes first-pass summaries of those records once the manifest has proven they're all present. It drafts the visit-prep notes I then edit. It handles synthesis, rephrasing, the compression of a long document into something I can scan — all the work where my eyes are the last step and a wrong word costs a second of my attention. That is judgment work, and judgment is what these models are genuinely good at.

The honest counter-case is that deterministic scripts earn their keep only under specific conditions. They are brittle where the input actually varies — the lab vendor changes an API field and my script breaks in a way a flexible agent would have shrugged off. They need maintenance; every one of them is a small standing liability on my time. And they cost more up front. Writing a prompt takes a minute; writing the records-intake script took an afternoon and a couple of rounds of debugging OCR edge cases. If the records bundles had been low-stakes, that afternoon would have been a bad trade.

## The decision rule

The line I draw now follows the shape of the requirement. The sophistication of the tool sits downstream of that call. When a step needs a judgment, and a human reviews the result before it counts, a model is the right instrument and often the best one available. When a step needs a guarantee — prove it ran, name what it touched, refuse rather than guess — and the failure mode is silent while the cost of a miss is high, I write the script. Prompts express intent. Scripts express contracts. Most of my workflow is intent, and I'm glad to have a good model carrying it. The handful of places that need a contract are the places I stopped asking a model to promise, and started making the computer keep its word.
