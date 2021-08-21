import {
    AfterViewInit,
    Directive,
    ElementRef,
    Input,
    Renderer2
  } from "@angular/core";
  
  @Directive({
    selector: "[bubblingText]"
  })
  export class BubblingTextDirective implements AfterViewInit {
    @Input() maxFontSize = 40;
    @Input() colorSchemeArray: string[]=[];
    @Input() position: "left" | "right" = "right";
    @Input() percentOfScreen =50;
  
    constructor(private elementRef: ElementRef, private renderer: Renderer2) {}
  
    ngAfterViewInit(): void {
      this.init();
      this.animateBackground();
    }
  
    private init(): void {
    }
  
    private animateBackground(): void {
      const renderer = this.renderer;
      const elementRef = this.elementRef;
      const chars = [...Array(26)].map((e, i) => (i + 10).toString(36));
  
      setInterval(() => {
        const duration = Math.floor(Math.random() * 15);
        const offset = Math.floor(Math.random() * this.percentOfScreen);
        const size = Math.floor(Math.random() * this.maxFontSize);
        // const color = this.colorSchemeArray[
        //   Math.floor(Math.random() * this.colorSchemeArray.length)
        // ];
        // console.log("color",color)
        const span = renderer.createElement("span");
        span.innerText = 0
        renderer.addClass(span, "animated-text");
  
        renderer.setStyle(span, "color", "white");
        renderer.setStyle(span, this.position, `${offset}vw`);
        renderer.setStyle(span, "font-size", `5px`);
        renderer.setStyle(span, "animation-duration", `${duration}s`);
        // renderer.setStyle(span, "color", color);
  
        renderer.appendChild(elementRef.nativeElement, span);
        setTimeout(() => {
          renderer.removeChild(
            this.elementRef.nativeElement,
            this.elementRef.nativeElement.firstChild
          );
        }, duration * 1000);
      }, 100);
    }
  }
  