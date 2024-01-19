export default function Section({ 'section-name': name, 'children': children }){
    console.log(name);
    console.log(children);
    return (
        <section id={`${name}-section`}>
            <div className={`${name}-content`}>
                {children}
            </div>
        </section>
    );
}